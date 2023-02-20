from django.urls import path

from categories.views import *

urlpatterns = [
    path('', categories_view, name='categories_view'),
    path('add/', category_add_view, name='category_add_view'),
    path('<int:pk>/edit/', category_edit_view, name='category_edit_view'),
    path('<int:pk>/delete/', category_delete_view, name='category_delete_view'),
]
