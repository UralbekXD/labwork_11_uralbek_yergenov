from django.shortcuts import render, redirect
from django.urls import reverse

from products.models import Product
from categories.models import Category


def products_view(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', context={
        'products': products,
    })


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'pk': product.pk,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'created_at': product.created_at.strftime('%d/%m/%Y %H:%M'),
        'category': product.category.name,
        'image': product.image,
    }

    return render(request, 'products/product.html', context=context)


def product_add_view(request):
    match request.method:
        case 'GET':
            categories = Category.objects.all()
            context = {
                'categories': categories,
            }
            return render(request, 'products/product_add.html', context=context)

        case 'POST':
            category_id = request.POST.get('category')
            category = Category.objects.get(pk=category_id)
            product = Product.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                price=request.POST.get('price'),
                image=request.POST.get('image'),
                category=category,
            )

            return redirect(reverse('product_view', kwargs={'pk': product.pk}))


def product_edit_view(request, pk):
    match request.method:
        case 'GET':
            product = Product.objects.get(pk=pk)
            categories = Category.objects.all()
            return render(request, 'products/product_edit.html', context={
                'product': product,
                'categories': categories,
            })

        case 'POST':
            category_id = request.POST.get('category')
            category = Category.objects.get(pk=category_id)

            product = Product.objects.get(pk=pk)
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.image = request.POST.get('image', '')
            product.category = category
            product.save()

            return redirect(reverse('product_view', kwargs={'pk': pk}))


def product_delete_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    return redirect('products_view')
