from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.homeView, name="home"),
    path('shop/', views.shopView, name="shop"),
    path('checkout/', views.checkoutView, name="checkout"),
    path('cart/', views.cartView, name="cart"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
