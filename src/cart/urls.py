from django.urls import path
from .views import index, addToCart, updateCart
app_name = 'cart'
urlpatterns = [
    path('',index, name="cart"),
    # path('addToCart/',addToCart, name="updateCart"),
    path('updateCart/',updateCart, name="updateCart"),
]