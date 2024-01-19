from .forms import ProductForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import *
from django.shortcuts import render, get_object_or_404, redirect



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
            print(request.POST)
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
def add_product(request):
    form = addProduct()
    if request.method == 'POST':
        # Handle form submission
        P_name = request.POST['P_name']
        P_desc = request.POST['P_desc']
        P_category_id = request.POST['P_category_id']
        P_curstock = request.POST['P_curstock']
        P_price = request.POST['P_price']
        P_rating = request.POST['P_rating']

        # Process the form data (save to the database or perform other actions)
        # For demonstration purposes, let's print the form data
        form_data = {
            'P_name': P_name,
            'P_desc': P_desc,
            'P_category_id': P_category_id,
            'P_curstock': P_curstock,
            'P_price': P_price,
            'P_rating': P_rating,
        }
        print(form_data)
    return render(request, 'addproduct.html', {'form': form})
def delete_product(request, product_id=None):
    product = get_object_or_404(productModel, P_id=product_id)
    product.delete()
    return redirect("/Product")

