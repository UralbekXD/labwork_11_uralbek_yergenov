from django.shortcuts import render, redirect

from categories.models import Category


def categories_view(request):
    categories = Category.objects.all()

    return render(request, 'categories/index.html', context={
        'categories': categories,
    })


def category_add_view(request):
    match request.method:
        case 'GET':
            return render(request, 'categories/category_add.html')

        case 'POST':
            Category.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
            )

            return redirect('categories_view')


def category_edit_view(request, pk):
    match request.method:
        case 'GET':
            category = Category.objects.get(pk=pk)
            return render(request, 'categories/category_edit.html', context={
                'category': category,
            })

        case 'POST':
            category = Category.objects.get(pk=pk)
            category.name = request.POST.get('name')
            category.description = request.POST.get('description')
            category.save()

            return redirect('categories_view')
