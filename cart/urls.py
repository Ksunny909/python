from django.conf.urls import path
from . import views

urlpatterns = [path('^$', views.cart_detail, name='cart_detail'),
               path('^add/(?P<doctor_id>\d+)/$', views.cart_add, name='cart_add'),
               path('^remove/(?P<doctor_id>\d+)/$', views.cart_remove,
                   name='cart_remove'), ]
