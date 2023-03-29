from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from .Forms import ProductForm

# product views

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    
    
def Create_Product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
