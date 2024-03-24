from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['agent', 'date_out', 'time_out', 'date_in', 'time_in', 'fuel', 'mileage', 'payment', 'notes']


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.Textarea)
