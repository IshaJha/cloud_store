from django.shortcuts import render
from datetime import datetime, timedelta
from products.models import Product
from cart.models import Cart
from .models import Order
from cloud_store.utils import calculateTotal


def createOrder(request):
    context = {"page":"Order Confirmed"}
    
    user = request.user

    # CHECK IF PRODUCTS IN CART ARE IN STOCK
    
    cart_objs = Cart.objects.filter(user=user, status='in_bag')
    for cart_obj in cart_objs:
        print(cart_obj)
        product = cart_obj.product
        quantity_ordered = cart_obj.quantity
        stock = product.in_stock
        if quantity_ordered<stock:
            print('success')
            # UPDATE PRODUCT QUANTITY

            product_obj = Product.objects.get(pk = product.pk)
            product_obj.in_stock = product_obj.in_stock - quantity_ordered#product object # update quantity
            product_obj.save()

            # CREATE ORDER OBJECT
            order_shipping_date = datetime.now() + timedelta(days=5)
            order_obj_new = Order.objects.create(user=user, order_shipping_date=order_shipping_date)
            order_obj_new.save()            
        else:
            print('error')# HOW WILL USERS GET NOTIFIED IF STOCK IS OVER

    # 
    
    # order_obj_new = Order.objects.create(user=user, order_shipping_date=order_shipping_date)
    # order_obj_new.save()


    return render(request, "home_page.html",context ) # redirect("cart:cart")

def orderList(request):
    #TRY USING CLASS VIEWS
    context = {}
    if request.user.is_authenticated:
        context["page"] = "Order List"
        # print(request.user)
        order_obj = Order.objects.filter(user = request.user)
        context["order_obj"] = order_obj
        # for order in order_obj:
        #     print(order.pk)
        #     print(order.user)
        #     # context["pk"] = order.pk
        #     # context["user"] = order.user
        # cart_objs = Cart.objects.filter() # this is order list there are multiple orders  
    else:
        context["page"] = "User Not logedin!!"
    return render(request, "orderList.html",context )
    

# """ All orders are seperated by the date and time they are ordered
#     To produce a list of orders 
#         1)  Select all orders of a User   
#         2)  for each order object select the product from cart using order_placed_date

#  """

def orderDetails(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        obj_pk = request.POST.get('order_pk')
        cart_objs = Cart.objects.filter(order_no = obj_pk)
        # print(cart_objs)
        # for obj in cart_objs:
        #     print(obj)
            
            
    context["cart_objs"] = cart_objs
    return render(request,'orderDetail.html', context)

    # order_obj = Order.objects.filter(user=request.user)
    # print(order_obj.order_placed_date)
    # print list of products in Order.order_placed_date