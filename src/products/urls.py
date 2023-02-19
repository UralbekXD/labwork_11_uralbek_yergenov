from django.urls import path

from products.views import products_view

urlpatterns = [
    path('', products_view),
    path('products/', products_view),
]
