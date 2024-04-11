from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import *
from admin.views import home
from employee.views import *

def login(request):
  #  modeldt = adminModel.objects.all()
        position = ""
        if request.method == 'POST':
            email_id = request.POST['email']
            passw = request.POST['password']
            try:
                 user_instance = adminModel.objects.get(email=email_id)
                 if user_instance.password == passw:
                          print(user_instance.password)
                          print(user_instance.name)
                          name = user_instance.name
                          position="admin"
                          request.session['email'] = user_instance.email
                          return home(request,name,position)
                 else:
                          return render(request, 'login.html', {'error': 'Incorrect password'})
            except adminModel.DoesNotExist:
                try:        
                   user_instance = empModel.objects.get(emp_email=email_id)
                   if user_instance.password == passw:
                          print(user_instance.password)
                          print(user_instance.emp_firstname)
                          name = user_instance.emp_firstname
                          position="emp"
                          return Employe_Hom(request,name,position)                 
                   else:
                          return render(request, 'login.html', {'error': 'Incorrect password'})
                except:
                    return render(request, 'login.html', {'error': 'User not found'})
               
        
        return HttpResponse(render(request,'login.html')) 

