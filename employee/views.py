from django.http import HttpResponse
from django.shortcuts import redirect, render
from admin.models import *
from employee.models import *


def Employe_Hom(request,name=None,position=""):
    modeldt = adminModel.objects.all()
    T_ord= ordersModel.objects.count()
    T_return= refundModel.objects.count()         
    return HttpResponse(render(request,'home_emp.html',{'position':position,'name':name,'admin':modeldt,'Tot_return':T_return,'Tot_ord':T_ord}))

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
def returnChange(request,return_id):
     if request.method == 'GET':
        data= refundModel.objects.get(return_id=return_id)
        return render(request,'returnChange.html',{"data":data})

     if request.method == 'POST':
        return_id = request.POST['o_id']
        status = request.POST['status']
        try:
            statusUpdate = refundModel.objects.get(return_id=return_id) 
            statusUpdate.return_status = status
            statusUpdate.save()
            return render(request, 'returnChange.html', {'alert_message': 'Product status updated successfully!'})

        except Exception as e:
            print("not updated")
            print(e)
            return redirect(request, 'orders')
def refund(request):
    refund = refundModel.objects.all()
    return HttpResponse(render(request,'returnStatus.html',{"refunds":refund}))


     
