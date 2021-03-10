from django.db import models
from django.conf import settings
# from django.db.models.signals import post_save
from products.models import Product
# Create your models here.
User = settings.AUTH_USER_MODEL

CART_ITEM_STATUS = (
    ("in_bag","In Bag"),
    ("ordered","Ordered"),
)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, primary_key=False)
    status = models.CharField(max_length = 120, default = 'in_bag', choices = CART_ITEM_STATUS)
    order_no = models.CharField(max_length = 120, null=True, blank=True, default=None)
    # order_placed_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank =True, null=True, default=None)
    #need a signal to update order_placed_date

    def __str__(self):
        return str(self.user)

# def user_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         Cart.objects.create(user=instance)

# post_save.connect(user_created_receiver, sender=User)