from django.shortcuts import render
from django.http import HttpResponse
from .models import adminModel 
# Create your views here.
def home(request):
    model = adminModel.objects.all()
    print(model)
    return HttpResponse("Hello World")
def index(request):
    return HttpResponse(render(request,'home.html'))
def login(request):
    return HttpResponse(render(request,'login.html'))