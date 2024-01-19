"""
URL configuration for ownamenity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index),
    path('admin/home.html', home),  
    path('admin/product.html', products, name="products"),
    path('admin/addProduct.html', add_product, name='add_product'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('admin/login.html', login),
    path('user/',include('userapp.urls')),
]
