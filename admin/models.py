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

class Category(models.Model):
    cate_id = models.IntegerField(primary_key=True)
    cate_name = models.CharField(max_length=20)

    class Meta:
        managed=False
        db_table = 'category'

class complaintModel(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_title = models.CharField(max_length=40)
    cust_id = models.IntegerField(db_index=True)
    c_status = models.TextField()
    c_desc = models.TextField()

    class Meta:
        managed=False
        db_table = 'complaint'

class CustMaterial(models.Model):
    Cate_id = models.IntegerField(db_index=True)
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=30)
    
    class Meta:
        managed=False
        db_table = 'cust_martial'

class MaterialType(models.Model):
    mate_cat_id = models.AutoField(primary_key=True)
    material_id = models.IntegerField(db_index=True)
    mat_price = models.IntegerField()
    mat_type = models.CharField(max_length=30)
    mat_img = models.CharField(max_length=200)
    mat_color = models.CharField(max_length=20)

    class Meta:
        managed=False
        db_table = 'mateial_type'

class SelectedMaterial(models.Model):
    customization_id = models.IntegerField(db_index=True)
    material_id = models.IntegerField(db_index=True)
    mate_desc = models.CharField(max_length=50)
    O_id = models.IntegerField()
    class Meta:
        managed=False
        db_table = 'selected_mat'

class  productModel(models.Model):
        # id = models.AutoField(primary_key=True)
    P_id = models.IntegerField(primary_key=True,max_length=10)
    P_name = models.CharField(max_length=30, null=False)
    P_desc = models.CharField(max_length=100, null=False)
    P_category_id = models.IntegerField(max_length=5,null=False)
    P_subcat_id = models.IntegerField(max_length=10,null=False)
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

from django.db import models

class Customization_req(models.Model):
    Cust_id = models.IntegerField(primary_key=True)  # Primary key field
    customization_id = models.IntegerField(unique=True)  # Primary key field
    c_name = models.CharField(max_length=20)  # Field for customization name
    c_desc = models.CharField(max_length=200)  # Field for customization description
    c_dimen = models.CharField(max_length=10)  # Field for customization dimensions
    c_img = models.CharField(max_length=200)  # Field for customization image URL
    c_date = models.DateField()  # Field for customization date
    c_status = models.CharField(max_length=10)  # Field for customization status
    class Meta:
        managed=False
        db_table = 'customization_request'
    
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

class CategoryModel(models.Model):
    Cate_id = models.IntegerField(primary_key=True)
    Cate_name = models.CharField(max_length=200)

    class Meta: 
        managed=False
        db_table= 'category'
class OrderProduct(models.Model):
    O_id = models.IntegerField(max_length=10)
    p_id = models.IntegerField()   
    p_name = models.IntegerField()   
    id = models.AutoField(primary_key=True) 
    P_quantity = models.IntegerField() 

    class Meta:
        managed=False
        db_table = 'order_product'
class statusModel(models.Model):
    o_id = models.IntegerField(primary_key=True)
    order_exp_date = models.DateField()
    delivery_date = models.DateField()
    order_status = models.CharField(max_length=50)
    emp_id = models.IntegerField()

    class Meta:
        managed=False
        db_table = 'order_status'
class OfferModel(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField(max_length=20)
    p_id = models.IntegerField()
    offer_type = models.CharField(max_length=50)
    discount_per = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    isActive = models.BooleanField(default=True)
    description = models.CharField(max_length=100)
    class Meta:
        managed=False
        db_table = 'offer'

class refundModel(models.Model):
    return_id= models.IntegerField(primary_key=True)
    O_id=models.IntegerField(max_length=10)
    return_status=models.CharField(max_length=100)
    return_price=models.IntegerField()
    return_tran_id=models.CharField(max_length=20)
        
    class Meta:
        managed=False
        db_table='order_refund_return'

class subCatModel(models.Model):
    sub_cat_id=models.IntegerField(primary_key=True)
    size=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    material_type=models.CharField(max_length=20)
    product_type=models.CharField(max_length=20)
    Cate_id=models.IntegerField()

    class Meta:
        managed=False
        db_table='sub_category'