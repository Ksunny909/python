from django.urls import path
from .views import HomePageView, PatientsListView, RecordsListView, SearchView
from . import views

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('patients', PatientsListView.as_view(), name='patients'),
path('records', RecordsListView.as_view(), name='records'),
path('search', SearchView.as_view(), name='search'),
path('^$', views.product_list, name='product_list'),
path('^(?P<category_slug>[-\w]+)/$', views.product_list,
                    name='product_list_by_category'),
path('^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,
                    name='product_detail'),


]
