
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
  
    #path('admin/', admin.site.urls),
    #path('/login', login),
    path('/home', home),  
    path('/product', products, name="products"),
    path('/Order', Orders, name="orders"),
    path('/User_List', User_List, name="user"),
    path('/emp', emp, name="emp"),
    #path('addProduct', add_product, name='add_product'),
    #path('/addCategory',add_Category,name='add_Category'),
    path('/category',category,name='category'),
    path('/edit-product/<int:product_id>', edit_product, name='edit_product'),
    path('/delete-product/<int:product_id>', delete_product, name='delete_product'),
<<<<<<< HEAD

=======
    path('/refund',refund,name="refund"),
    path('/sub-cat/<int:Cate_id>',subcat,name="subcategory"),
    
>>>>>>> d83a4f948f4421d10b9ac8af99b6bc68dea626fb
    # path('refund-pay/<int:refund>',)
    # path('login', login),
]

