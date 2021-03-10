from django.shortcuts import render, redirect
from django.conf import settings
# from django.contrib.auth.models import User
from .models import Cart
from products.models import Product
from cloud_store.utils import calculateTotal
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

User = settings.AUTH_USER_MODEL

def index(request):
    # shipping_charge = 70
    cart_obj = Cart.objects.filter(user=request.user, status='in_bag')
    # sub_total = 0
    # for obj in cart_obj:
    #     sub_total = sub_total + int(obj.product.price)
    total, sub_total, shipping_charge = calculateTotal(cart_obj)
    
    total = sub_total + shipping_charge 
    context = {
        "page":"Cart",
        "cart_obj":cart_obj,
        "sub_total":sub_total,
        "shipping_charge":shipping_charge,
        "total":total,
    }

    print(cart_obj)
    return render(request, "cart.html", context)

# NOT USING IT addToCart VIEW
def addToCart(request):# if product already in cart then increase quantity of product (To be done)
    context = {"page":"addToCart"}
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        user_obj = request.user # issue if user not logedin
        product = Product.objects.filter(pk=product_id)
        product_obj = None
        if len(product) == 1:
            product_obj = product.first()
            

        # print("product_obj")
        # print(product_obj)
        # print("user_obj")
        # print(user_obj)

        if product_obj is not None:
            print(product_obj.pk)
            cart_obj = Cart.objects.filter(product = product_obj, user = request.user, status='in_bag')
            print(len(cart_obj))
            if len(cart_obj)>0:
                obj = cart_obj.first()
                # print(obj.qu)
                obj.quantity = obj.quantity + 1
                obj.save()
            else:
                cart_obj_new = Cart.objects.create(user=user_obj,product=product_obj)
                cart_obj_new.save()
        else:
            context['error'] = "error"
        

    return redirect("products:productsList")
    # return render(request, "products/productsList",context )


# def removeFromCart():
#     pass

def updateCart(request):
    # 1) USER REQUESTS TO DELETE OR ADD TO CART - how will user send those requests???
    if request.method == 'POST':
        print(request.POST) #USER REQUEST TYPE  'product_id':['2'], 'action_type': ['delete']}
        action_type = request.POST.get('action_type') #USER REQUEST TYPE  'product_id':['2'], 'action_type': ['delete']}>
        product_id = request.POST.get('product_id') #USER REQUEST TYPE  'product_id':['2'], 'action_type': ['delete']}>
        # add_to_cart
        # delete
        # NOW CHECK IF PRODUCT.QUANTITY IS > 1  IN CART
        product_obj = Product.objects.get(pk = product_id)

        
        # quantity = cart_obj.quantity
        try:
            cart_obj = Cart.objects.get(user = request.user, status = 'in_bag', product = product_obj)
            quantity = cart_obj.quantity
            
            if (action_type == 'add_to_cart'):
                print('INCREASE QUANTITY || add_to_cart')
                cart_obj.quantity = cart_obj.quantity + 1
                cart_obj.save()
                # pass
                # INCREASE QUANTITY
            elif (action_type == 'delete'):
                if quantity > 1:
                    print('DECREASE QUANTITY || delete')
                    cart_obj.quantity = cart_obj.quantity - 1
                    cart_obj.save()
                elif quantity == 1:
                    cart_obj.delete()
                # DECREASE QUANTITY
            # here increase quantity 
        except ObjectDoesNotExist:
            print("CREATE NEW OBJECT")
            cart_obj_new = Cart.objects.create(user=request.user,product=product_obj)
            cart_obj_new.save()

    #
    return render(request, "home_page.html",{"page":"updateCart"} )