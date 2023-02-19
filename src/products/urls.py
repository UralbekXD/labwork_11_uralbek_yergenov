from django.urls import path

from products.views import products_view, product_view

urlpatterns = [
    path('', products_view),
    path('products/', products_view),
    path('products/<int:pk>', product_view),
]
