from django.db import models

# Create your models here.
class adminModel(models.Model):
        # id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='admin_name',max_length=20, null=True)
    password = models.CharField(db_column='password',max_length=20, null=True)
    email = models.CharField(db_column='email_id',max_length=30, primary_key=True)
    
    class Meta:
        managed=False
        db_table = 'admin'
    # def __str__(self): #this is to show the name in the admin panel, you will understand in the next tutorial
    #     return self.name #even if you dont write this function, you will not face any issues
class productModel(models.Model):
        # id = models.AutoField(primary_key=True)
    P_id = models.IntegerField(primary_key=True,max_length=10)
    P_name = models.CharField(max_length=30, null=False)
    P_desc = models.CharField(max_length=100, null=False)
    P_category_id = models.IntegerField(max_length=5,null=False)
    P_curstock = models.IntegerField(max_length=10,null=False)
    P_price = models.IntegerField(max_length=10,null=False)
    P_rating = models.FloatField(null=False)
    
    class Meta:
        managed=False
        db_table = 'product'


class ordersModel(models.Model):
        # id = models.AutoField(primary_key=True)
    O_id = models.IntegerField(max_length=10,primary_key=True)
    Cust_id = models.IntegerField(max_length=10,null=False)
    O_date = models.DateField(null=False)
    O_address = models.CharField(max_length=100,null=False)
    o_total_amt = models.IntegerField(max_length=5,null=False)
    o_disc_price = models.IntegerField(max_length=5,null=False)
    O_payment_mtd = models.CharField(max_length=30,null=False)
    O_type = models.CharField(max_length=20,null=False)
    
    class Meta:
        managed=False
        db_table = 'orders'

class UserModel(models.Model):
        # id = models.AutoField(primary_key=True)
    Cust_id = models.IntegerField(max_length=10,primary_key=True)
    First_name = models.CharField(max_length=20, null=False)
    Last_name = models.CharField(max_length=20, null=False)
    Email_id = models.CharField(max_length=30, null=False)
    Contact_no = models.BigIntegerField(null=False)
    Dob = models.DateField(null=True)
    Password = models.CharField(max_length=10, null=False)
    Address = models.CharField(max_length=100, null=True)
    Pincode = models.IntegerField(null=True)
    Profile_pic = models.CharField(max_length=200, null=True)
    
    class Meta:
        managed=False
        db_table = 'customer'

class ProductImage(models.Model):
    p_img_id = models.IntegerField(primary_key=True) 
    p_img_link = models.CharField(max_length=200)
    p_id = models.IntegerField(max_length=10) 
    
    class Meta:
            managed=False
            db_table = 'product_image' 