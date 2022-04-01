from django import forms

DOCTOR_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddDoctorForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=DOCTOR_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)