from django.urls import path
from .views import Create_Product, ProductListView, update_product, delete_product


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', Create_Product, name='create_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
]

