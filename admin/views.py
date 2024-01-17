from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admin(request):
    return HttpResponse("Hello World")
def index(request):
    return HttpResponse(render(request,'home.html'))
def login(request):
    return HttpResponse(render(request,'login.html'))