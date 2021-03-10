from cart.models import Cart

def calculateTotal(cart_obj):
    shipping_charge = 70
    # cart_obj = Cart.objects.filter(user=user)
    sub_total = 0
    for obj in cart_obj:
        sub_total = sub_total + int(obj.product.price)
    
    total = sub_total + shipping_charge
    return total, sub_total, shipping_charge