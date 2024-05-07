from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from products.models import Product
from accounts.models import Address

ORDER_TYPE=[
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ]
class Order(models.Model):
    user=models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=75,choices=ORDER_TYPE,default='Recieved')
    code=models.CharField(max_length=50,default=generate_code)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    copoun=models.ForeignKey('Copoun',on_delete=models.SET_NULL,blank=True,null=True)
    total=models.FloatField(null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class Order_Detail(models.Model):
    order=models.ForeignKey(Order,related_name='detatil_order',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='detail_product',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)
    



class Copoun(models.Model):
    code=models.CharField(max_length=120)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(null=True,blank=True)
    quantity=models.IntegerField()
    discount=models.FloatField()

    def __str__(self):
        return self.code

CART_TYPE=[
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
    ]
class Cart(models.Model):
    user=models.ForeignKey(User,related_name='cart_user',on_delete=models.CASCADE)
    status=models.CharField(max_length=75,choices=CART_TYPE)
    copoun=models.ForeignKey(Copoun,related_name='cart_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total_with_copon=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class Cart_Detail(models.Model):
    cart=models.ForeignKey(Cart,related_name='detatil_cart',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='cart_detail_product',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.cart)
