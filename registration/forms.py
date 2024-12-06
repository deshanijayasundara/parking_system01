# forms.py
from django import forms
from .models import Customer, Payment, Parking

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'nic_number', 'contact_number', 'email']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_holder_name', 'expiry_date', 'cvv']

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['vehicle_number', 'vehicle_type', 'check_in_time', 'duration', 'preferred_location']