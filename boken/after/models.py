from django.db import models

# Create your models here.
class Bo(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=288)
    author=models.CharField(max_length=20)
    datas=models.DateTimeField(auto_now_add=True)
