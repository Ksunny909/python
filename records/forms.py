from django import forms
from .models import Record


class RecordCreateForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['last_name', 'first_name', 'email']
    password1 = forms.CharField(initial='Aa12345678', widget=forms.TextInput(
      attrs={'class': 'form-control', 'type': 'password', 'name': 'password', 'readonly': True}),  #
                                label="Пароль")
    password2 = None