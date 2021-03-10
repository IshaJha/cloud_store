from django.urls import path
from .views import getProductList, getProductDetail

app_name = 'products'
urlpatterns = [
     path('', getProductList, name ='productsList'),
     # path('<int:pk>/', getProductDetail, name ='productDetail'),
     path('<slug:slug>/', getProductDetail, name ='productDetail'),
]