from django.urls import path
from .views import createOrder, orderDetails, orderList

app_name = 'order'

urlpatterns = [
    path('',orderList, name="orderList"),
    path('details/', orderDetails, name="orderDetails"),
    path('createOrder/',createOrder, name="createOrder"),
]