from datetime import datetime
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
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ProductImage, productModel, subCatModel

def products(request):
    # Fetch all product images, products, and subcategories
    pro_images = ProductImage.objects.all()
    products = productModel.objects.all()
    subcats = subCatModel.objects.all()

    if request.method == 'POST':
        search_query = request.POST.get('search', '')

        if search_query:
            products = products.filter(P_name__icontains=search_query)

            return render(request, 'Product.html', {
                'products': products,
                'pro_img': pro_images,
                'subcats': subcats,
                'search_query': search_query
            })

    return render(request, 'Product.html', {'products': products,'pro_img': pro_images,'subcats': subcats})

def complaints(request):
    comps = complaintModel.objects.all()
    return HttpResponse(render(request,'complaints.html',{'comps':comps}))

def Orders(request):
    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                orders = ordersModel.objects.filter(O_date__range=(start_date, end_date)).order_by('-O_date')
            except ValueError:
                orders = ordersModel.objects.none()
        else:
            orders = ordersModel.objects.all().order_by('-O_date')
    else:
        orders = ordersModel.objects.all().order_by('-O_date')

    return render(request, 'orderList.html', {'orders': orders})

def report(request):
    if request.method == "POST":
             orders = ordersModel.objects.all()
             start_date = request.POST['start_date']
             end_date = request.POST['end_date']
    
             if start_date and end_date:
              # Parse start_date and end_date strings into datetime objects
              start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
              end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
              
              orders = orders.filter(O_date__range=(start_date, end_date))
              return render(request, 'ord-report.html', {'orders': orders})
    orders = ordersModel.objects.all()
    products= OrderProduct.objects.all()
    productsname= OrderProduct.objects.all()
    print(orders)
    return HttpResponse(render(request,'ord-report.html',{'orders':orders,'products':products,"PN":productsname}))


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
def accept(request,customization_id):
    req = Customization_req.objects.get(customization_id=customization_id)
    if request.method == 'POST':
        print("this is post enter")
        total_amt = request.POST['total_amt']
        print("got the total" )
        print(total_amt)
        order= ordersModel.objects.create(
                            Cust_id=req.Cust_id,
                            O_date=datetime.today(),
                            O_address="",
                            o_total_amt=total_amt,
                            o_disc_price=0,
                            O_payment_mtd="",
                            O_type="customize",
         )
        print("order saved")
        return redirect('/customize_requests')
def selacted_mat(request,customization_id):
    customization_id=customization_id
    materialId= SelectedMaterial.objects.filter(customization_id=customization_id)
    materialDetails=MaterialType.objects.all()
    return render(request,'selacted_mat.html',{"matIds":materialId,"matDetails":materialDetails,"customization_id":customization_id})
    
def selacted_matrials(request,o_id):
    materialId= SelectedMaterial.objects.filter(O_id=o_id)
    print(materialId)
    materialDetails=MaterialType.objects.all()
    return render(request,'selacted_mat_orders.html',{"matIds":materialId,"matDetails":materialDetails})
    

def delete_offer(request, offer_id):
    product = get_object_or_404(OfferModel, offer_id=offer_id)
    product.delete()
    return redirect('/offer')

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

def add_offer(request):
    products = productModel.objects.all()
    pro_img = ProductImage.objects.all()
    if request.method == 'POST':
        # Process the form data here
        offer_name = request.POST.get('offer_name')
        offer_type = request.POST.get('offer_type')
        discount_value = request.POST.get('discount_value')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        selected_products = request.POST.getlist('products')  # Get list of selected product IDs
        print(selected_products)
        for p_id in selected_products:
            try:
                product = productModel.objects.get(P_id=p_id)
                offer = OfferModel.objects.create(
                    offer_name=offer_name,
                    offer_type=offer_type,
                    discount_value=discount_value,
                    start_date=start_date,
                    end_date=end_date,
                    description=description,
                    p_id=p_id
                )
               # product.P_price * discount_value / 100
                product.save()
            except productModel.DoesNotExist:
                # Handle case where product with given ID does not exist
                # You can log an error or display a message to the user
                pass
        return redirect('offer')  
    return render(request, 'addOffer.html', {'products': products ,"pro_img":pro_img})

def apply_offer_discount(offer, selected_products):
    for product_id in selected_products:
        try:
            product = productModel.objects.get(P_id=product_id)
            product.P_price -= offer.discount_value
            product.save()
        except productModel.DoesNotExist:
            pass
def offer(request):
     details = OfferModel.objects.all()
     ProDetails = productModel.objects.all()
     return HttpResponse(render(request,'offer.html',{"details":details,"ProDetails":ProDetails}))
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
            return render(request, 'editMateOpt.html',{"msg": e})
def delete_MatOpt(request,mate_cat_id,mateid):
        product = get_object_or_404(MaterialType, mate_cat_id=mate_cat_id)
        product.delete()
        print("deleted")
        return MatType(request,msg="Option Removed",mateid=mateid)
def refunds(request):
    refund = refundModel.objects.all()
    return HttpResponse(render(request,'refund.html',{"refunds":refund}))
def order_products(request,o_id):
     if request.method == 'GET':
        data = OrderProduct.objects.all()
        return render(request,'order_product.html',{"data":data,"id":o_id})
def selected_mat(request,o_id):
     if request.method == 'GET':
        data = OrderProduct.objects.all()
        return render(request,'order_product.html',{"data":data,"id":o_id})

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