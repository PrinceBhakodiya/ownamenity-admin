from django.http import HttpResponse
from django.shortcuts import redirect, render
from admin.models import *
from employee.models import *


def Employe_Hom(request,name=None,position=""):
    modeldt = adminModel.objects.all()
    T_pro= productModel.objects.count()
    T_ord= ordersModel.objects.count()
    T_usr= UserModel.objects.count()         
    return HttpResponse(render(request,'home_emp.html',{'position':position,'name':name,'admin':modeldt,'Tot_pro':T_pro,'Tot_ord':T_ord,'Tot_usr':T_usr}))

def order(request):
    orders = ordersModel.objects.all()
    status = statusModel.objects.all()
    return HttpResponse(render(request,'orderList_emp.html',{'orders':orders,"statuses":status}))
# Create your views here.
def edit_status(request,order_id):
     if request.method == 'GET':
        data= statusModel.objects.get(o_id=order_id)
        return render(request,'editStatus.html',{"data":data})

     if request.method == 'POST':
        o_id = request.POST['o_id']
        status = request.POST['status']
        try:
            statusUpdate = statusModel.objects.get(o_id=o_id) 
            statusUpdate.order_status = status
            statusUpdate.save()
            return render(request, 'editStatus.html', {'alert_message': 'Product status updated successfully!'})

        except Exception as e:
            print("not updated")
            print(e)
            return redirect(request, 'orders')


     
