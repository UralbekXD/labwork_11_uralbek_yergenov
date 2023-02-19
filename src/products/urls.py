from django.urls import path

from products.views import products_view, product_view, product_add_view

urlpatterns = [
    path('', products_view, name='products_view'),
    path('<int:pk>/', product_view, name='product_view'),
    path('add/', product_add_view, name='product_add_view'),
]
