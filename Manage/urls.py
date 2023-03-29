from django.urls import path
from .views import Create_Product, ProductListView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', Create_Product, name='create_product'),
]

