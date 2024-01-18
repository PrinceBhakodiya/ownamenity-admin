from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import adminModel

# Create your views here.
def home(request):
    modeldt = adminModel.objects.all()
    # print(model)
    return HttpResponse(render(request,'home.html',{'admin':modeldt}))
def index(request):
    return HttpResponse(render(request,'home.html'))
def login(request):
  #  modeldt = adminModel.objects.all()
        if request.method == 'POST':
            email_id = request.POST['email']
            passw = request.POST['password']
            print(email_id)
            try:
                user_instance = adminModel.objects.get(email=email_id)
                if user_instance.password == passw:
                    print(user_instance.password)
                    print(user_instance.name)                    
                    return redirect('/admin/home.html',{'name':user_instance.name})
                else:
                    return render(request, 'login.html', {'error': 'Incorrect password'})
            except adminModel.DoesNotExist:
                return render(request, 'login.html', {'error': 'User not found'})
        
        return HttpResponse(render(request,'login.html'))  