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
class Product(models.Model):
    p_id = models.IntegerField(primary_key=True, max_length=10)
    p_name = models.CharField(max_length=30, null=False)
    p_desc = models.CharField(max_length=100, null=False)
    p_category_id = models.IntegerField(max_length=5, null=False)
    p_curstock = models.IntegerField(max_length=10, null=False)
    p_price = models.IntegerField(max_length=10, null=False)
    p_rating = models.FloatField(null=False)

    class Meta:
        managed = False
        db_table = 'product'

    def to_dict(self):
        return {
            'p_id': self.p_id,
            'p_name': self.p_name,
            'p_desc': self.p_desc,
            'p_category_id': self.p_category_id,
            'p_curstock': self.p_curstock,
            'p_price': self.p_price,
            'p_rating': self.p_rating,
            'images': [image.to_dict() for image in self.product_image.all()]
        }
class productImageModel(models.Model):
        # id = models.AutoField(primary_key=True)
    P_img_id = models.IntegerField(primary_key=True,max_length=10)
    P_img_link = models.CharField(max_length=30, null=False)
    p = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE)
    
    class Meta:
        managed=False
        db_table = 'product_image'
    def to_dict(self):
        return {
            'p_img_id': self.P_img_id,
            'p_img_link': self.P_img_link,
            'p_id': self.p.pk
        }

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

class Customer(models.Model):
        # id = models.AutoField(primary_key=True)
    cust_id = models.IntegerField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email_id = models.CharField(max_length=30, null=False)
    contact_no = models.IntegerField(null=False)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    profile_pic = models.CharField(max_length=200, null=True)
    
    class Meta:
        managed=False
        db_table = 'customer'  
    def to_dict(self):
        return {
            'cust_id': self.cust_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_id': self.email_id,
            'contact_no': self.contact_no,
            'dob': str(self.dob) if self.dob else None,
            'password': self.password,
            'address': self.address,
            'pincode': self.pincode,
            'profile_pic': self.profile_pic,
        }