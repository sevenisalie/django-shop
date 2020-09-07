from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.homeView, name='home'),
    path('shop/', views.shopView, name='shop'),
    path('checkout/', views.checkoutView, name='checkout'),
    path('cart/', views.cartView, name='cart'),
]
