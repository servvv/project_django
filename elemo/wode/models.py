from django.db import models

# Create your models here.
class Customer(models.Model):
    uid=models.ForeignKey('User', null=True, blank=True,on_delete=models.SET_NULL)
    password=models.CharField(max_length=64)
    pay_password=models.CharField(max_length=64)
    loyalty=models.IntegerField()
    vips=models.SmallIntegerField()
    adress_id=models.IntegerField()
    head=models.ImageField(default='')
    ex_password=models.SmallIntegerField()
    wallet=models.IntegerField()
    phone=models.CharField(max_length=11)
    wechat=models.CharField(max_length=12)
    qq=models.CharField(max_length=10)
    add_time=models.DateTimeField(auto_now_add=True)
class xf_Address(models.Model):
    uid=models.ForeignKey('User', null=True, blank=True,on_delete=models.SET_NULL)
    adress=models.CharField(max_length=200)
class User(models.Model):
    username=models.CharField(max_length=20)

