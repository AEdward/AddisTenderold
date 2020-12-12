from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51HuDtaLLRgPcFpZt1watXvelSray78T6uyh3kuVTW8JPe9HAEYuxnkn2lWt8OSs3t3o7hYzmJ2hDp2KzZbO4yv6W00loVvVF40"

# Create your views here.

def pay(request):
	return render(request, 'payment/index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['FullName'],
			source=request.POST['stripeToken']
			)
		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Payment"
			)

	return redirect(reverse('payment:success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'payment/success.html', {'amount':amount})