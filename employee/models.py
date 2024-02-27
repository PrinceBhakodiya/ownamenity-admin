from django.db import models
class empModel(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_firstname = models.CharField(max_length=20)
    emp_lastlame = models.CharField(max_length=20)
    emp_email = models.CharField(max_length=30)
    emp_contact = models.IntegerField()
    password = models.CharField(max_length=20)
    emp_DOJ = models.DateField()
    emp_salary = models.IntegerField()
    emp_address = models.CharField(max_length=100)
    emp_img = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=20)

    class Meta:
       managed=False
       db_table = 'employee'

class statusModel(models.Model):
    o_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField(unique=True)
    order_exp_date = models.DateField()
    delivery_date = models.DateField()
    order_status = models.CharField(max_length=50)
    emp_id = models.IntegerField()

    class Meta:
        managed=False
        db_table = 'order_status'