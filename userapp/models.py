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
    p_id = models.IntegerField(primary_key=True, max_length=10,db_column='p_id')
    p_name = models.CharField(max_length=30, null=False,db_column='p_name')
    p_desc = models.CharField(max_length=100, null=False,db_column='p_desc')
    p_category_id = models.IntegerField(max_length=5, null=False,db_column='p_category_id')
    p_curstock = models.IntegerField(max_length=10, null=False,db_column='p_curstock')
    p_price = models.IntegerField(max_length=10, null=False,db_column='p_price')
    p_rating = models.FloatField(null=False,db_column='p_rating')
    # p_image= product_image.all()
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
class Category(models.Model):
    cate_id = models.IntegerField(db_column='Cate_id', primary_key=True)  # Field name made lowercase.
    cate_name = models.CharField(db_column='Cate_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Orders(models.Model):
        # id = models.AutoField(primary_key=True)
    O_id = models.TextField(primary_key=True)  # Primary key field
    Cust_id = models.IntegerField(max_length=10,null=False)
    o_date = models.DateField(null=False)
    o_address = models.CharField(max_length=100,null=False)
    o_total_amt = models.IntegerField(max_length=5,null=False)
    o_disc_price = models.IntegerField(max_length=5,null=False)
    o_payment_mtd = models.CharField(max_length=30,null=False)
    o_type = models.CharField(max_length=20,null=False)
    
    class Meta:
        managed=False
        db_table = 'orders'
     


class OrderProduct(models.Model):
        # id = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)

    order_id = models.ForeignKey(Orders, related_name='Orders', on_delete=models.CASCADE, db_column='O_id')
    p_id=models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, db_column='p_id')
    
    class Meta:
        managed=False
        db_table = 'order_product'
     

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email_id = models.CharField(max_length=30, null=False, unique=True)
    contact_no = models.CharField(max_length=15, null=True, unique=True)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    profile_pic = models.CharField(max_length=200, null=True)

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

    class Meta:
        managed=False
        db_table = 'customer'
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Make sure the field name is 'cust'

    class Meta:
        managed=False
        db_table = 'cart'


class CartProduct(models.Model):
    id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,db_column='cart_id')
    P_id= models.ForeignKey(Product, on_delete=models.CASCADE,db_column='p_id')
    p_quantity = models.PositiveIntegerField(default=1,db_column='p_quantity')
    P_add_date = models.DateField(auto_now_add=True, db_column='P_add_date')

    class Meta:
        managed = False
        db_table = 'cart_product'
   
class OrderStatus(models.Model):
    o_id = models.TextField(primary_key=True,db_column="o_id")
    order_no = models.ForeignKey(Cart, on_delete=models.CASCADE,db_column='order_id')
    order_exp_date= models.DateField(auto_now_add=True, db_column='order_exp_date')
    delivery_date = models.DateField(auto_now_add=True, db_column='delivery_date')
    order_status= models.TextField( db_column='order_status')

    class Meta:
        managed = False
        db_table = 'order_status'
   