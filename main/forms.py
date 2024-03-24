from django import forms
from .models import Rental, Feedback

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['agent', 'date_out', 'time_out', 'date_in', 'time_in', 'fuel', 'mileage', 'payment', 'notes']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
