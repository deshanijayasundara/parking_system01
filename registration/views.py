# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm, PaymentForm, ParkingForm

def get_started(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        payment_form = PaymentForm(request.POST)
        parking_form = ParkingForm(request.POST)

        if customer_form.is_valid() and payment_form.is_valid() and parking_form.is_valid():
            customer = customer_form.save()
            payment = payment_form.save()
            parking = parking_form.save(commit=False)
            parking.customer = customer
            parking.payment = payment
            parking.save()
            return redirect('success')
    else:
        customer_form = CustomerForm()
        payment_form = PaymentForm()
        parking_form = ParkingForm()

    return render(request, 'get_started.html', {
        'customer_form': customer_form,
        'payment_form': payment_form,
        'parking_form': parking_form,
    })

def success(request):
    return render(request, 'success.html')