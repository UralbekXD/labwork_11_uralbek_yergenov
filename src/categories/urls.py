from django.urls import path

from categories.views import categories_view, category_add_view, category_edit_view

urlpatterns = [
    path('', categories_view, name='categories_view'),
    path('add/', category_add_view, name='category_add_view'),
    path('<int:pk>/edit/', category_edit_view, name='category_edit_view'),
]
