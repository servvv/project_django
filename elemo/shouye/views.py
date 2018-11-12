from django.shortcuts import render
from .models import Seller
# Create your views here.
def index(request):
    #print('这里没问题')
    se=Seller
    osj=Seller.objects.all()
    cont={'b':osj}
    return render(request,'index.html',cont)
def mine(request):
    return render(request,'mine.html')
def mine(request):
    return render(request,'mine.html')
def mine(request):
    return render(request,'mine.html')
def sell(request):
    return render(request,'小媳妇儿凉皮/小媳妇儿凉皮.html')