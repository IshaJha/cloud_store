from django.db import models
from django.conf import settings
from datetime import datetime
from django.db.models.signals import post_save
from cart.models import Cart

User = settings.AUTH_USER_MODEL

# Create your models here.
ORDER_STATUS = (
    ("confirmed","Confirmed"),
    ("dispatched","Dispatched"),
    ("on-to-delivery","On delivery to you"),
    ("delivered","Delivered"),
)
class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    status_of_order = models.CharField(max_length = 120, default = 'in_bag', choices = ORDER_STATUS)
    order_placed_date = models.DateTimeField(auto_now_add=True)
    order_shipping_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank =True, null=True, default=None)
    #ShippingAddress
    # order_shipping_date =auto_now_add + time takne to diliver( to be calculated by the distance between the sender and the reciver)

    def __str__(self):
        return str(self.pk)


def order_created_signal(sender, instance, *args, **kwargs):
    cart_obj = Cart.objects.filter(user=instance.user, status='in_bag')#get() returned more than one Cart -- it returned 3!
    for obj in cart_obj:
        print(obj.pk)
        print(obj.status)
        obj.order_no = instance.pk
        obj.status = 'ordered'
        #find in_stock of each product in cart
        obj.save()

post_save.connect(order_created_signal, sender=Order)