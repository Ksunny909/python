from django import forms
from .models import Record


class RecordCreateForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['last_name', 'first_name', 'email']
