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
