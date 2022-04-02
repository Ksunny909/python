from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from shop.models import Patient, Record, Doctor
from django.db.models import Q
from cart.forms import CartAddDoctorForm
from django.shortcuts import render, get_object_or_404
#from .models import Category, Doctor

class HomePageView(TemplateView):
    template_name = 'home.html'

class PatientsListView(ListView):
 template_name = "patient.html"
 model = Patient
 context_object_name = "list_of_all_patients"

class RecordsListView(ListView):
 template_name = "records.html"
 model = Record
 context_object_name = "list_of_all_records"


class SearchView(ListView):
 template_name = "search.html"
 model = Record
 context_object_name = "list_of_all_records"

#def doctor_list(request, category_slug=None):
 # category = None
  #categories = Category.objects.all()
  #doctors = Doctor.objects.filter(available=True)
  #if category_slug:
 #  category = get_object_or_404(Category, slug=category_slug)
   #doctors = doctors.filter(category=category)
  #return render(request, 'shop/product/list.html',
  #              {'category': category, 'categories': categories,
  #               'doctors': doctors})


def doctor_detail(request, id, slug):
 doctor = get_object_or_404(Doctor, id=id, slug=slug, available=True)
 cart_doctor_form = CartAddDoctorForm()
 return render(request, 'shop/detail.html', {'doctor': doctor, 'cart_doctor_form': cart_doctor_form})

#def get_queryset(self):
 # query = self.request.GET.get('q')
 # return Record.objects.filter(
 #  Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query)
 # )
