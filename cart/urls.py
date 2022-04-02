from django.urls import path
from . import views

urlpatterns = [path('cart_detail', views.cart_detail, name='cart_detail'),
               path('add/(<doctor_id>\d+)', views.cart_add, name='cart_add'),
               path('remove/(<doctor_id>\d+)', views.cart_remove,
                   name='cart_remove'), ]
