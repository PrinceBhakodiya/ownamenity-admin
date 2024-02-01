
from django.urls import path,include
from admin.views import *
from admin import views


urlpatterns = [
  
    path('admin',include('admin.urls')),
    path('user/',include('userapp.urls')),
]