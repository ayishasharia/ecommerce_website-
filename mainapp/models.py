from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class user_1(models.Model):
    gender=models.CharField(max_length=255,null=True)
    phone=models.IntegerField(null=True)
    dob=models.CharField(max_length=255,null=True)
    
    address=models.CharField(max_length=255,null=True)
    UserF=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
class product_model(models.Model):
    p_id=models.AutoField
    p_name=models.CharField(max_length=255,null=True)
    p_category=models.CharField(max_length=255,null=True)
    p_desc=models.CharField(max_length=255,null=True)
    p_price=models.IntegerField(null=True)
    p_image=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.p_name 
    
class cart_item(models.Model):
    item=models.ForeignKey(product_model,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now=True)
    quantity=models.IntegerField(null=True,default=1)
    price=models.FloatField(null=True)
    is_ordered=models.BooleanField(default=False,null=True)
    
    def subtotal(self):
        return self.quantity * self.price

class cart_Model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    items=models.ManyToManyField(cart_item)
