from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Doctor
from .cart import Cart
from .forms import CartAddDoctorForm

@require_POST
def cart_add(request, doctor_id):
  cart = Cart(request)
  doctor = get_object_or_404(Doctor, id=doctor_id)
  form = CartAddDoctorForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(doctor=doctor, quantity=cd['quantity'], update_quantity=cd['update'])
  return redirect('cart:cart_detail')
#def doctor_detail(request, id, slug):
#    doctor = get_object_or_404(Doctor, id=id, slug=slug, available=True)
#    cart_doctor_form = CartAddDoctorForm()
#    return render(request, 'shop/doctor/detail.html', {'doctor': doctor, 'cart_doctor_form': cart_doctor_form})
def cart_remove(request, doctor_id):
  cart = Cart(request)
  doctor = get_object_or_404(Doctor, id=doctor_id)
  cart.remove(doctor)
  return redirect('cart:cart_detail')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})