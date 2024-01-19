from itertools import product
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Customerview(request):
    if request.method == "GET":    
        cust = Customer.objects.all()
        serialized_data = [customer.to_dict() for customer in cust]
        return JsonResponse( serialized_data, safe=False)
    
    elif request.method == "POST":
        data = request.POST  # You might need to use request.POST or request.body based on your fronten
        new_customer = Customer.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email_id=data['email'],
            contact_no=data['contact_no'],
            password=data['password']
            # Add other fields here
        )
        return JsonResponse({"customer": new_customer.to_dict(),"msg":"Registered Success"}, safe=False)

@csrf_exempt 
def LoginView(request):
    if request.method == "GET":
        return HttpResponse("Login")
    if request.method == "POST":
        data = request.POST  # You might need to use request.POST or request.body based on your fronten
        email = data.get('email')
        pw = data.get('password')
        
        try:
            customer =Customer.objects.get(email_id=email)
            try:
                if(customer.password==pw):
                    return JsonResponse({"data": customer.to_dict(),"msg":"Login Success"}, safe=False)
                else:
                    return JsonResponse({"msg1":"Incorrect Password","msg2":"Login Failed"}, safe=False)     
            except:
                return JsonResponse({"msg1":"Incorrect Password","msg2":"Login Failed"}, safe=False)   
        except :
             return JsonResponse({"msg1":"Email Not Found","msg2":"Login Failed"}, safe=False)
    return JsonResponse({"msg": "Invalid request method"}, safe=False)

@csrf_exempt
def ProductView(request,p_id=None):
   if request.method == "GET":  
        p_id = request.GET.get('p_id')  
        if p_id is not None:
            try:
                # Try to retrieve the product with the specified p_id
                product = Product.objects.get(p_id=p_id)
                serialized_data = product.to_dict()
                return JsonResponse(serialized_data, safe=False)
            except Product.DoesNotExist:
                # Handle the case when the product with the specified p_id does not exist
                return JsonResponse({'error': 'Product not found'}, status=404)
        else:        
            product_image = productImageModel.objects.all()
            print(product_image)
            products = Product.objects.all()
            serialized_data = [
                
                product.to_dict()
                for product in products
                
            ]
            return JsonResponse(serialized_data, safe=False)