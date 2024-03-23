
from django.urls import path,include
from admin.views import *
from employee.views import *
from ownamenity.views import *

urlpatterns = [
    #path('orders/',orders),
    path('home', home),  
    path('Employe_Home',Employe_Hom),
    path('product', products, name="products"),
    path('custMat', custMat, name="custMat"),
    path('add_MateOpt', add_MateOpt, name="add_MateOpt"),
    path('add_CustMat', add_CustMat, name="add_CustMat"),
    path('Order', Orders, name="Order"),
    path('complaints', complaints, name="complaints"),
    path('order', order, name="order"),
    path('User_List', User_List, name="user"),
    path('emp', emp, name="emp"),
    path('refunds',refunds,name="refunds"),
    path('add_product', add_product, name='add_product'),
    path('return_status', refund, name='return_status'),
    path('order-products/<int:order_id>', order_products, name='order_products'),
    path('addCategory',add_Category,name='add_Category'),
    path('category',category,name='category'),
    path('edit-product/<int:product_id>', edit_product, name='edit_product'),
    path('MatType/edit_MateOpt/<int:mate_cat_id>',edit_MateOpt ,name='edit_product'),
    path('MatType/<int:mateid>', MatType, name='edit_product'),
    path('order-product/<int:order_id>', edit_status, name='edit_status'),
    path('return_change/<int:return_id>', returnChange, name='return_change'),
    path('delete-product/<int:product_id>', delete_product, name='delete_proudct'),
    path('MatType/delete_MatOpt/<int:mate_cat_id>/<int:mateid>', delete_MatOpt, name='delete_MatOpt'),
    path('',login),
    path('login',login),
    path('admin',include('admin.urls')),
    path('employee/',include('employee.urls')),
    path('user/',include('userapp.urls')),
    # path('offer', offer, name="offer"),
    path('refund',refund,name="refund"),
    path('sub-cat',subcat,name="subcategory"),
    path('add_subCategory',add_subCategory,name="add_subCategory"),
    path('sub-cat/<int:Cate_id>',subcat,name="subcategory"),

]
