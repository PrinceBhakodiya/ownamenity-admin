from itertools import product
from datetime import *
from django.http import JsonResponse,HttpResponse
from .models import *
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Customerview(request):
    if request.method == "GET":    
        cust = Customer.objects.all()
        serialized_data = [customer.to_dict() for customer in cust]
        return JsonResponse( serialized_data, safe=False)
    
    elif request.method == "POST":
   
        data = request.POST  # You might need to use request.POST or request.body based on your fronten
        if data['email'] and Customer.objects.filter(email_id=data['email']).exists():
            return JsonResponse({"msg": "Email already exists"}, status=400)

        # Check if a customer with the same contact number already exists (if contact number is not empty)
        if data['contact_no'] and Customer.objects.filter(contact_no=data['contact_no']).exists():
            4
            return JsonResponse({"msg": "Contact number already exists"}, status=400)

        new_customer = Customer.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email_id=data['email'],
            contact_no=data['contact_no'],
            password=data['password']
            # Add other fields here
        )
        cart = Cart.objects.create(cust_id=new_customer.cust_id)

        return JsonResponse({"data": new_customer.to_dict(),"msg":"Registered Success"}, safe=False)

@csrf_exempt
def DeleteCustomer(request):

    try:
            cust_id = request.GET.get('cust_id')

            # Try to get the customer record from the database
            customer = Customer.objects.get(cust_id=cust_id)
            
            # Delete the customer record
            customer.delete()
            
            return JsonResponse({"msg": "Customer deleted successfully"}, status=200)
        
    except Customer.DoesNotExist:
            # Handle the case when the customer with the specified cust_id does not exist
            return JsonResponse({"msg": "Customer not found"}, status=404)
    
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
                    return JsonResponse({"msg":"Incorrect Password"}, safe=False)     
            except:
                return JsonResponse({"msg":"Incorrect Password"}, safe=False)   
        except :
             return JsonResponse({"msg":"Email Not Found"}, safe=False)
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


@csrf_exempt
def CategoryView(request,p_id=None):
   if request.method == "GET":  
        p_id = request.GET.get('c_id')  
        if p_id is not None:
            try:
                # Try to retrieve the product with the specified p_id
                product = Product.objects.get(p_id=p_id)
                serialized_data = product.to_dict()
                return JsonResponse(serialized_data, safe=False)
            except Product.DoesNotExist:
                # Handle the case when the product with the specified p_id does not exist
                return JsonResponse({'error': 'Category not found'}, status=404)
        else:        
            product_image = productImageModel.objects.all()
            print(product_image)
            products = Product.objects.all()
            serialized_data = [
                
                product.to_dict()
                for product in products
                
            ]
            return JsonResponse(serialized_data, safe=False)
        
# fetch cart        
@csrf_exempt
def fetch_cart(request):
    if request.method == "GET":
        email = request.GET.get('email')
        try:
            customer = Customer.objects.get(email_id=email)
            cart = Cart.objects.get(cust_id=customer)
            cart_products = CartProduct.objects.filter(cart_id=cart)
            products = []
            for cart_product in cart_products:
                    product = cart_product.P_id
                    product_details = {
                        'id':cart_product.id,
                        'product_id': product.p_id,
                        'product_name': product.p_name,
                        'product_desc': product.p_desc,
                                                'product_price': product.p_price,

                        'product_image': product.product_image.first().P_img_link if product.product_image.exists() else None,
                        'quantity': cart_product.p_quantity,
                        'add_date': cart_product.P_add_date.strftime('%Y-%m-%d')
                    }

                    products.append(product_details)
                    

            total_amount = sum(cart_product.P_id.p_price * cart_product.p_quantity for cart_product in cart_products)
            return JsonResponse({"cart": products,"amount":total_amount})
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Customer not found"}, status=404)
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":

        
        data = request.POST  # You might need to use request.POST or request.body based on your frontend

        # Extract necessary information from the request data
        email = data.get('email')
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))  # Default quantity is 1 if not provided

        try:
            # Retrieve the customer object based on the provided email
            customer = Customer.objects.get(email_id=email)

            # Check if the customer has a cart
            cart, created = Cart.objects.get_or_create(cust_id=customer)

            # Retrieve the product object based on the provided product ID
            product = Product.objects.get(p_id=product_id)

            # Check if the product is already in the cart
            cart_product, created = CartProduct.objects.get_or_create(cart_id=cart, P_id=product)

            # If the product is already in the cart, update the quantity
            if not created:
                cart_product.p_quantity += quantity
                cart_product.save()
                return JsonResponse({"msg": "Product updated in the cart successfully"}, status=200)
            else:
                # If the product is not in the cart, create a new entry in the CartProduct table
                cart_product.p_quantity = quantity
                cart_product.save()
                return JsonResponse({"msg": "Product added to the cart successfully"}, status=200)

        except Customer.DoesNotExist:
            return JsonResponse({"error": "Customer not found"}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def delete_cart(request):
    if request.method == "POST":
        data = request.POST  # You might need to use request.POST or request.body based on your frontend

        # Extract necessary information from the request data
        email = data.get('email')

        try:
            # Retrieve the customer object based on the provided email
            customer = Customer.objects.get(email_id=email)

            # Check if the customer has a cart
            cart = Cart.objects.filter(cust_id=customer).first()
            Cart_product = CartProduct.objects.filter(cart_id=cart)

            if cart:
                # Delete the cart
                for items in Cart_product:
                    items.delete()
                return JsonResponse({"msg": "Cart deleted successfully"}, status=200)
            else:
                return JsonResponse({"error": "Cart not found for the customer"}, status=404)

        except Customer.DoesNotExist:
            return JsonResponse({"error": "Customer not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def remove_from_cart(request):
    if request.method == "POST":
        data = request.POST  # You might need to use request.POST or request.body based on your frontend

        # Extract necessary information from the request data
        cart_product_id = data.get('cart_product_id')

        try:
            # Retrieve the cart product object based on the provided cart_product_id
            cart_product = CartProduct.objects.get(id=cart_product_id)

            # Delete the cart product
            cart_product.delete()

            return JsonResponse({"msg": "Product removed from cart successfully"}, status=200)

        except CartProduct.DoesNotExist:
            return JsonResponse({"error": "Cart product not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)
@csrf_exempt
def checkout(request):
    if request.method == "POST":
        # Extract data from the request
        email = request.POST.get('email')
        address = request.POST.get('address')

        try:
            # Retrieve the customer's cart
            customer_cart = Cart.objects.get(cust_id__email_id=email)

            # Retrieve cart items
            cart_products = CartProduct.objects.filter(cart_id=customer_cart)

            if not cart_products:
                return JsonResponse({"error": "Cart is empty"}, status=400)

            # Calculate total amount and discounted price
            total_amount = sum(cart_product.P_id.p_price * cart_product.p_quantity for cart_product in cart_products)
            discounted_price = 0  # Assuming no discount for now

            # Create order
           # Create order
            order = Orders.objects.create(
                Cust_id=customer_cart.cust.cust_id,
                o_date=datetime.now().date(),
                o_address=address,
                o_total_amt=total_amount,
                o_disc_price=discounted_price,
                o_payment_mtd="online",
                o_type="standard",
            )
            print(order.o_id)
            # Create order products
            for cart_product in cart_products:
                OrderProduct.objects.create(
                    order_id=order,  # Assign the entire order object
                    p_id=cart_product.P_id,
                )

            # Empty the cart after checkout
            cart_products.delete()

            return JsonResponse({"msg": "Order placed successfully", "order_id": order.o_id}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)
        
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def orders(request):
    if request.method == "GET":
        # Extract data from the request
        email = request.GET.get('email')

        try:
            # Retrieve the customer's cart
            customer=Customer.objects.get(email_id=email)
                     # Retrieve orders associated with the customer
            orders = Orders.objects.filter(Cust_id=customer.cust_id)

            # Prepare response data
            order_list = []

            for order in orders:
                order_data = {
                    'order_id': order.o_id,
                    'order_date': order.o_date.strftime('%Y-%m-%d'),
                    'order_address': order.o_address,
                    'total_amount': order.o_total_amt,
                    'discounted_price': order.o_disc_price,
                    'payment_method': order.o_payment_mtd,
                    'order_type': order.o_type,
                    'products': []
                }
    # Retrieve products associated with the order
                order_products = OrderProduct.objects.filter(order_id=order.o_id)
                for order_product in order_products:
                    product_data = {
                        'product_id': order_product.p_id.p_id,
                        'product_name': order_product.p_id.p_name,
                        # 'quantity': order_product.P_quantity,
                        'price_per_unit': order_product.p_id.p_price
                    }
                    order_data['products'].append(product_data)

                order_list.append(order_data)

            return JsonResponse({"orders": order_list}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)
        
    return JsonResponse({"error": "Invalid request method"}, status=400)
