from django.shortcuts import render

# Create your views here.


def estore(request):
    context = {}
    return render(request, 'estore/store.html', context)


def cart(request):
    context = {}
    return render(request, 'estore/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'estore/checkout.html', context)

def home(request):
    context = {}
    return render(request, 'estore/main.html', context)
