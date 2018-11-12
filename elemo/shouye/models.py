from django.db import models

# Create your models here.
class Food(models.Model):
    f_name=models.CharField(max_length=20)
    msq=models.IntegerField()
    price=models.IntegerField()
    discount=models.IntegerField()
    describe=models.CharField(max_length=120)
    img=models.ImageField(default='')
    praise=models.IntegerField()
    business_id=models.ForeignKey('Seller', null=True, blank=True,on_delete=models.SET_NULL)
class Seller(models.Model):
    sname=models.CharField(max_length=20)
    address=models.CharField(max_length=120)
    starting_price=models.IntegerField()
    dist_price=models.IntegerField()
    seller_phhoto=models.ImageField(default='')
