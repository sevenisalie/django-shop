from django.shortcuts import render
from .models import *

# Create your views here.
def homeView(request):
    context={}
    return render(request, 'shop/home.html', context)

def shopView(request):
    products = Product.objects.all()


    context={
    "products": products,
    }
    return render(request, 'shop/shop.html', context)

def cartView(request):

    if request.user.is_authenticated:           # this is to make a cart for a signed in user, or a non authenitcated user, aka an anonymous person
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []                  #empty list represents anonymos user
        order = {'get_cart_items': 0, 'get_cart_total': 0}      #to display cart totals for non-logged in user

    context={
    "items": items,
    "order": order,
    }
    return render(request, 'shop/cart.html', context)

def checkoutView(request):

    if request.user.is_authenticated:           # this is to make a cart for a signed in user, or a non authenitcated user, aka an anonymous person
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []                  #empty list represents anonymos user
        order = {'get_cart_items': 0, 'get_cart_total': 0}      #to display cart totals for non-logged in user

    context={
    'items': items,
    'order': order,
    }
    return render(request, 'shop/checkout.html', context)
