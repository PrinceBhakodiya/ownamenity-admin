
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
      path('/home', home),
    # path('admin/', admin.site.urls),
    # path('/',login),
    # path('/login', login),
    # path('/product', products, name="products"),
    # path('/orders', orders, name="orders"),
    # path('/users', user, name="user"),
    # path('/emp', emp, name="emp"),
    # path('/addProduct', add_product, name='add_product'),
    # path('/addCategory',add_Category,name='add_Category'),
    # path('/category',category,name='category'),
    # path('/edit-product/<int:product_id>', edit_product, name='edit_product'),
    # path('/delete-product/<int:product_id>', delete_product, name='delete_product'),
    # path('login', login),
]

