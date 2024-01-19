from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import *

# Create your views here.
def home(request):
    modeldt = adminModel.objects.all()
    T_pro= productModel.objects.count()
    T_ord= ordersModel.objects.count()
    T_usr= UserModel.objects.count()
    return HttpResponse(render(request,'home.html',{'admin':modeldt,'Tot_pro':T_pro,'Tot_ord':T_ord,'Tot_usr':T_usr}))
def index(request):
    return HttpResponse(render(request,'home.html'))
def login(request):
  #  modeldt = adminModel.objects.all()
        if request.method == 'POST':
            email_id = request.POST['email']
            passw = request.POST['password']
            try:
                user_instance = adminModel.objects.get(email=email_id)
                if user_instance.password == passw:
                    print(user_instance.password)
                    print(user_instance.name)
                    name = user_instance.name
                    
                    return home(request)
                else:
                    return render(request, 'login.html', {'error': 'Incorrect password'})
            except adminModel.DoesNotExist:
                return render(request, 'login.html', {'error': 'User not found'})
        
        return HttpResponse(render(request,'login.html')) 
def products(request):
    products = productModel.objects.all()
    return HttpResponse(render(request,'Product.html',{'products':products}))

def my_view(request):
    return render(request, 'tamp.html', {})

