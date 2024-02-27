
# from django.contrib import admin
from django.urls import path,include
from userapp.views import *
# from userapp.views import CustomerViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'customer',CustomerViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create',Customerview),
        path('delete',DeleteCustomer),

    path('login',LoginView),
    path('product',ProductView ,name='product_view'),
    path('category',CategoryView ,name='category_view'),
        #   path('product?<int:p_id>', ProductView, name='product_detail'),  # <int:p_id> captures the p_id parameter
    path('cart/', fetch_cart, name='cart-detail'),
    path('cart/add',add_to_cart, name='addtocart'),
    path('cart/delete',delete_cart, name='deletecart'),
    path('cart/deleteproduct',remove_from_cart, name='deletproduct'),
    path('cart/checkout',checkout, name='checkout'),
    path('orders',orders, name='orders'),

    

]
