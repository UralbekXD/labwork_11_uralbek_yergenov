from django.shortcuts import render

from products.models import Product


def products_view(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', context={
        'products': products,
    })
