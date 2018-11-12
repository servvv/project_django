from django.db import models
from shouye.models import Seller,Food
from wode.models import Customer,xf_Address

# Create your models here.
class Order(models.Model):
    customer_id=models.ForeignKey(Customer, null=True, blank=True,on_delete=models.SET_NULL)
    sname_id=models.ForeignKey(Seller, null=True, blank=True,on_delete=models.SET_NULL)
    f_id=models.ForeignKey(Food, null=True, blank=True,on_delete=models.SET_NULL)
    spnum=models.IntegerField()
    zzje=models.IntegerField()
    order_status=models.CharField(max_length=20)
    order_nu=models.IntegerField()
class Order_detail(models.Model):
    order_id=models.ForeignKey(Order, null=True, blank=True,on_delete=models.SET_NULL)
    sname_id=models.ForeignKey(Seller, null=True, blank=True,on_delete=models.SET_NULL)
    customer_id=models.ForeignKey(Customer, null=True, blank=True,on_delete=models.SET_NULL)
    address_id=models.ForeignKey(xf_Address, null=True, blank=True,on_delete=models.SET_NULL)
    f_id=models.ForeignKey(Food, null=True, blank=True,on_delete=models.SET_NULL)
class History(models.Model):
    order_id=models.ForeignKey(Order, null=True, blank=True,on_delete=models.SET_NULL)
class Elaluate(models.Model):
    shopid=models.ForeignKey(Seller, null=True, blank=True,on_delete=models.SET_NULL)
    orderid=models.ForeignKey(Order,null=True, blank=True,on_delete=models.SET_NULL)
    userid=models.ForeignKey(Customer, null=True, blank=True,on_delete=models.SET_NULL)
    gondsScore=models.IntegerField()
    serviceScore=models.IntegerField()
    content=models.CharField(max_length=120)
    image=models.ImageField(default='')
    isShow=models.BooleanField(default=True)