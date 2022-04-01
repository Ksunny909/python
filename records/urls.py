from django.urls import path
from . import views
urlpatterns = [
  path('create/', views.record_create, name='record_create'),
]
