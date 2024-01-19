
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index),
    path('admin/home.html', home),  
    path('admin/product.html', products, name="products"),
    path('admin/addProduct.html', add_product, name='add_product'),
    path('delete-product/<int:product_id>', delete_product, name='delete_product'),
    path('admin/login.html', login),
    path('user/',include('userapp.urls')),
]
