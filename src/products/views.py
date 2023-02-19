from django.shortcuts import render

from products.models import Product


def products_view(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', context={
        'products': products,
    })


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'created_at': product.created_at.strftime('%d/%m/%Y %H:%M'),
        'category': product.category.name,
        'image': product.image,
    }

    return render(request, 'products/product.html', context=context)
