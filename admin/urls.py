
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
  
   #path('admin/', admin.site.urls),
    path('/',home),
    path('/login', login),
    path('/home', home),  
    path('/product', products, name="products"),
    path('/addProduct', add_product, name='add_product'),
    path('/delete-product/<int:product_id>', delete_product, name='delete_product'),
    # path('login', login),
]
