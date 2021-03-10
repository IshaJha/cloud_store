# get total price of all products in cart
from .models import Cart
def get_subtotal(user):
    cart_obj = Cart.objects.filter(user = user)
    print(cart_obj)
