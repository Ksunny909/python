from cart.cart import Cart
from django.shortcuts import render

from .forms import RecordCreateForm
from .models import RecordItem
#from .tasks import record_created
def record_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = RecordCreateForm(request.POST)
    if form.is_valid():
      record = form.save()
      for item in cart:
        RecordItem.objects.create(record=record, doctor=item['doctor'], price=item['price'], quantity=item['quantity'])
      cart.clear()
      return render(request, 'records/record/created.html', {'record': record})
    else:
      form = RecordCreateForm()
      return render(request, 'records/record/create.html', {'cart': cart, 'form': form})
  #cart.clear()
# launch asynchronous task
