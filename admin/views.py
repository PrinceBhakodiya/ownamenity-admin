from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import *
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request,name=None):
    modeldt = adminModel.objects.all()
    T_pro= productModel.objects.count()
    T_ord= ordersModel.objects.count()
    T_usr= UserModel.objects.count()
    return HttpResponse(render(request,'home.html',{'name':name,'admin':modeldt,'Tot_pro':T_pro,'Tot_ord':T_ord,'Tot_usr':T_usr}))
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
                    return home(request,name)
                else:
                    return render(request, 'login.html', {'error': 'Incorrect password'})
            except adminModel.DoesNotExist:
                return render(request, 'login.html', {'error': 'User not found'})
        
        return HttpResponse(render(request,'login.html')) 
def products(request):
    Pro_image= ProductImage.objects.all()
    products = productModel.objects.all()
    print(Pro_image)
    print(products)
    return HttpResponse(render(request,'Product.html',{'products':products,'pro_img':Pro_image}))
def orders(request):
    orders = ordersModel.objects.all()
    return HttpResponse(render(request,'orderList.html',{'orders':orders}))
def user(request):
    user = UserModel.objects.all()
    return HttpResponse(render(request,'UserList.html',{'user':user}))

def my_view(request):
    return render(request, 'tamp.html', {})
def add_product(request):
    if request.method == 'POST':
        P_id = request.POST['P_id']
        print(P_id)
        p_name = request.POST['name']
        P_desc = request.POST['P_desc']
        P_category_id = request.POST['P_category_id']
        P_curstock = request.POST['P_curstock']
        P_price = request.POST['P_price']
        P_rating = request.POST['P_rating']
        try:
            product= productModel.objects.create(P_id=P_id
                                                 ,P_name=p_name
                                                 ,P_desc=P_desc
                                                 ,P_category_id=P_category_id
                                                 ,P_curstock=P_curstock
                                                 ,P_price=P_price
                                                 ,P_rating=P_rating
                                               )
            product.save()
            return products(request)
        except Exception as e:
            print(e)
    return render(request, 'addProduct.html')
def delete_product(request, product_id):
    product = get_object_or_404(productModel, P_id=product_id)
    product.delete()
    return redirect("Product.html") 

def edit_product(request,product_id):
     if request.method == 'GET':
        data= productModel.objects.get(P_id=product_id)
        return render(request,'editProduct.html',{"data":data})

     if request.method == 'POST':
        P_id = request.POST['P_id']
        p_name = request.POST['name']
        P_desc = request.POST['P_desc']
        P_category_id = request.POST['P_category_id']
        P_curstock = request.POST['P_curstock']
        P_price = request.POST['P_price']
        P_rating = request.POST['P_rating']
        try:
            product= productModel.objects.update(P_id=P_id
                                                 ,P_name=p_name
                                                 ,P_desc=P_desc
                                                 ,P_category_id=P_category_id
                                                 ,P_curstock=P_curstock
                                                 ,P_price=P_price
                                                 ,P_rating=P_rating
                                               )
            product.save()
            return HttpResponse(render(request,'Product.html',{"msg":"Product Updated Successfully"}))
        except Exception as e:
            print(e)
     return redirect(request, 'product')

def category(request):
    category = CategoryModel.objects.all()
    return HttpResponse(render(request,'category.html',{"category":category}))
def add_Category(request):
     if request.method == 'POST':
        c_id = request.POST['C_id']
        c_name = request.POST['C_name']
        try:
            categor= CategoryModel.objects.create(Cate_id=c_id,Cate_name=c_name)
            categor.save()
            return category(request)
        except Exception as e:
            print(e)
     return render(request, 'addCategory.html')

