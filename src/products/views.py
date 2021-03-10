# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, "home_page.html", {"page":"Products"})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def getProductList(request):
    product_list = Product.objects.all()
    context = {
        "product_list":product_list,
    }
    return render(request,"products/list.html",context)

def getProductDetail(request, *args, **kwargs):
    product = Product.objects.get(slug = kwargs['slug'])
    context = {
        "product": product,
    }
    return render(request,"products/detail.html",context)