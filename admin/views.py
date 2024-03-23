from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin.models import *
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request,name=None,position=""):
    modeldt = adminModel.objects.all()
    T_pro= productModel.objects.count()
    T_ord= ordersModel.objects.count()
    T_usr= UserModel.objects.count()         
    return HttpResponse(render(request,'home.html',{'position':position,'name':name,'admin':modeldt,'Tot_pro':T_pro,'Tot_ord':T_ord,'Tot_usr':T_usr}))
def index(request):
    return HttpResponse(render(request,'home.html'))
# def login(request):
#   #  modeldt = adminModel.objects.all()
#         position = ""
#         if request.method == 'POST':
#             email_id = request.POST['email']
#             passw = request.POST['password']
#             try:
#                  user_instance = adminModel.objects.get(email=email_id)
#                  if user_instance.password == passw:
#                           print(user_instance.password)
#                           print(user_instance.name)
#                           name = user_instance.name
#                           position="admin"
#                           return request,name,position)
#                  else:
#                           return render(request, 'login.html', {'error': 'Incorrect password'})
#             except adminModel.DoesNotExist:
#                 try:
#                    user_instance = empModel.objects.get(emp_email=email_id)
#                    if user_instance.password == passw:
#                           print(user_instance.password)
#                           print(user_instance.emp_firstname)
#                           name = user_instance.emp_firstname
#                           position="emp"
#                           return home(request,name,position)                 
#                    else:
#                           return render(request, 'login.html', {'error': 'Incorrect password'})
#                 except:
#                     return render(request, 'login.html', {'error': 'User not found'})
               
        
#         return HttpResponse(render(request,'login.html')) 
def products(request, msg=""):
    pro_images = ProductImage.objects.all()
    products = productModel.objects.all()
    subcats = subCatModel.objects.all()
    print(pro_images)
    print(products)
    print(subcats)
    return render(request, 'Product.html', {'products': products, 'pro_img': pro_images, 'subcats': subcats, 'msg': msg})

def complaints(request):
    comps = complaintModel.objects.all()
    return HttpResponse(render(request,'complaints.html',{'comps':comps}))
def Orders(request):
    orders = ordersModel.objects.all()
    products= OrderProduct.objects.all()
    productsname= OrderProduct.objects.all()
    print(orders)
    return HttpResponse(render(request,'orderList.html',{'orders':orders,'products':products,"PN":productsname}))
def User_List(request):
    user = UserModel.objects.all()
    return HttpResponse(render(request,'UserList.html',{'user':user}))
def emp(request):
    emp = empModel.objects.all()
    return HttpResponse(render(request,'empList.html',{'emp':emp}))
def my_view(request):
    return render(request, 'tamp.html', {})
def add_product(request):
    if request.method == 'GET':
        category = CategoryModel.objects.all()
        sub_cat = subCatModel.objects.all()
        return render(request,'addProduct.html',{"categories":category,"sub_cat":sub_cat})
    if request.method == 'POST':
        print("command :  it inside")
        p_image = request.POST['image']
        p_name = request.POST['name']
        P_desc = request.POST['P_desc']
        P_category_id = request.POST['P_category_id']
        sub_cat_id = request.POST['sub_cat_id']
        P_curstock = request.POST['P_curstock']
        P_price = request.POST['P_price']
        print("command :  it got post data")
        print(p_image,p_name,P_desc,P_category_id,sub_cat_id,P_curstock,P_price,P_rating)
        try:
            product= productModel.objects.create(
                                                  P_name=p_name
                                                 ,P_desc=P_desc
                                                 ,P_category_id=P_category_id
                                                 ,P_subcat_id=sub_cat_id
                                                 ,P_curstock=P_curstock
                                                 ,P_price=P_price
                                                 ,P_rating=1 
                                               )
            latest_product = productModel.objects.latest('P_id')
            pid=latest_product.P_id
            print(pid)
            try:
                pro_image= ProductImage.objects.create(p_id=pid
                                                    ,p_img_link=p_image
                                                    )
                return products(request,msg="product added")
            except Exception as e:
                print(e)
                return render(request, 'addProduct.html')
        except:
            return render(request, 'addProduct.html')
def add_subCategory(request):
    if request.method == 'GET':
        category = CategoryModel.objects.all()
        return render(request,'add_subCate.html',{"categories":category})
    if request.method == 'POST':
        print("command :  it inside")
        Cate_id = request.POST['Cate_id']
        product_type = request.POST['product_type']
        material_type = request.POST['material_type']
        color = request.POST['color']
        size = request.POST['size']
        print("command :  it got post data")
        product= subCatModel.objects.create(      Cate_id=Cate_id
                                                 ,product_type=product_type
                                                 ,material_type=material_type
                                                 ,color=color
                                                 ,size=size
                                               )
        return render(request, 'add_subCate.html')
def delete_product(request, product_id):
    product = get_object_or_404(productModel, P_id=product_id)
    product.delete()
    return redirect('/product')

def edit_product(request,product_id):
     if request.method == 'GET':
        data= productModel.objects.get(P_id=product_id)
        dataimage= ProductImage.objects.get(p_id=product_id)
        category = CategoryModel.objects.all()
        return render(request,'editProduct.html',{"data":data,"categories":category,"dataimage":dataimage})

     if request.method == 'POST':
        P_id = request.POST['P_id']
        p_name = request.POST['name']
        p_image = request.POST['P_image']
        print("image name")
        print(p_image)
        P_desc = request.POST['P_desc']
        P_category_id = request.POST['P_category_id']
        P_curstock = request.POST['P_curstock']
        P_price = request.POST['P_price']
        P_rating = request.POST['P_rating']
        try:
            product= productModel.objects.get(P_id=P_id)
            product.P_name=p_name
            product.P_desc=P_desc
            product.P_category_id=P_category_id
            product.P_curstock=P_curstock
            product.P_price=P_price
            product.P_rating=P_rating
           # productI= ProductImage.objects.get(P_id=P_id)
           # productI.p_img_link=p_image
            product.save()
            if(p_image != ""):
             productImg= ProductImage.objects.get(p_id=P_id)
             productImg.p_img_link=p_image
             productImg.save()
            #productI.save()
            return HttpResponse(render(request,'editProduct.html',{"msg":"Product Updated Successfully"}))
        except Exception as e:
            print("not updated")
            print(e)
            return render(request, 'editProduct.html', {"msg": e})

def category(request):
    category = CategoryModel.objects.all()
    return HttpResponse(render(request,'category.html',{"categories":category}))
def custMat(request):
    Materials = CustMaterial.objects.all()
    return HttpResponse(render(request,'CustMat.html',{"Materials":Materials}))
# def offer(request):
#     details = OfferModel.objects.all()
#     return HttpResponse(render(request,'offer.html',{"details":details}))
def MatType(request,mateid,msg=""):
    Materials = MaterialType.objects.all()
    print(mateid)
    return HttpResponse(render(request,'MateType.html',{"Materials":Materials,"matId":mateid,"msg":msg}))
def add_Category(request):
     if request.method == 'POST':
        c_name = request.POST['C_name']
        try:
            categor= CategoryModel.objects.create(Cate_name=c_name)
            return category(request)
        except Exception as e:
            print(e)
     return render(request, 'addCategory.html')
def add_CustMat(request):
     if request.method == 'GET':
        category = CategoryModel.objects.all()
        return render(request,'addCustMat.html',{"categories":category})

     if request.method == 'POST':
        Cate_id = request.POST['Cate_id']
        material_name = request.POST['material_name']
        try:
            categor= CustMaterial.objects.create(Cate_id=Cate_id,material_name=material_name)
            return custMat(request)
        except Exception as e:
            print(e)
     return render(request, 'addCustMat.html')
def add_MateOpt(request):
     if request.method == 'GET':
        materials = CustMaterial.objects.all()
        return render(request,'addMateOpt.html',{"materials":materials})
     if request.method == 'POST':
        Cate_id = request.POST['material_id']
        mat_price = request.POST['price']
        mat_type=request.POST['name']
        mat_img=request.POST['image']
        mat_color=request.POST['color']
        print(Cate_id)
        try:
            categor= MaterialType.objects.create(material_id=Cate_id,
                                                 mat_price=mat_price,
                                                 mat_type=mat_type,
                                                 mat_img=mat_img,
                                                 mat_color=mat_color,
                                                 )
            print("adddone")
            return MatType(request,msg="add")
        except Exception as e:
            print(e)
            return render(request,'addMateOpt.html')
def edit_MateOpt(request,mate_cat_id):
     if request.method == 'GET':
        print(mate_cat_id)
        data = MaterialType.objects.get(mate_cat_id=mate_cat_id)
        materials = CustMaterial.objects.all()
        return render(request,'editMateOpt.html',{"data":data,"materials":materials})
     if request.method == 'POST':
        material_id = request.POST['material_id']
        mat_price = request.POST['price']
        mat_type=request.POST['name']
        mat_img=request.POST['image']
        mat_color=request.POST['color']
        try:
            mate= MaterialType.objects.get(mate_cat_id=mate_cat_id)
            mate.mat_price=mat_price
            mate.mat_type=mat_type
            if(mat_img != ""):
             mate.mat_img=mat_img
            mate.mat_color=mat_color
            mate.save()
            return HttpResponse(render(request,'editMateOpt.html',{"msg":"Product Updated Successfully"}))
        except Exception as e:
            print("not updated")
            print(e)
            return render(request, 'editMateOpt.html', {"msg": e})
def delete_MatOpt(request,mate_cat_id,mateid):
        product = get_object_or_404(MaterialType, mate_cat_id=mate_cat_id)
        product.delete()
        print("deleted")
        return MatType(request,msg="Option Removed",mateid=mateid)
def refunds(request):
    refund = refundModel.objects.all()
    return HttpResponse(render(request,'refund.html',{"refunds":refund}))
def order_products(request,order_id):
     if request.method == 'GET':
        data = OrderProduct.objects.all()
        return render(request,'order_product.html',{"data":data,"id":order_id})

     
def subcat(request,Cate_id):
    if request.method == 'GET':
        subcat = subCatModel.objects.all()
        print(Cate_id)
        categorys=Category.objects.get(cate_id=Cate_id)
        return HttpResponse(render(request,'subCategory.html',{"subcats":subcat,"cat_id":Cate_id}))     
def delete_subcate(request, sub_cat_id, Cate_id):
    data = get_object_or_404(subCatModel, sub_cat_id=sub_cat_id)
    data.delete()
    print("deleted")
    return subcat(request, msg="category remove", Cate_id=Cate_id)