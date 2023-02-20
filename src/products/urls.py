from django.urls import path

from products.views import products_view, product_view, product_add_view, product_edit_view, product_delete_view

urlpatterns = [
    path('', products_view, name='products_view'),
    path('<int:pk>/', product_view, name='product_view'),
    path('add/', product_add_view, name='product_add_view'),
    path('<int:pk>/edit/', product_edit_view, name='product_edit_view'),
    path('<int:pk>/delete/', product_delete_view, name='product_delete_view'),
]
