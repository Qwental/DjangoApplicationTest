from django.shortcuts import render

# Create your views here.
from products.models import *


def index(request):
    context = {
        'title': 'Shop Application',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
