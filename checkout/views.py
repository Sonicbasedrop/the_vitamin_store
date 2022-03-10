from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPvIkK1iSt89ZFsLeHqjN5uQPHDVYJqdSqzQHqHzwqH6TniK0544G4nRRGLl3fhvUwwUQWNDwgSwZq1g2E42hwY00RVbLsPgb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
