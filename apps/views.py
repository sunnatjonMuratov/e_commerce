from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .utils import remove_last_character

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            # Remove the last character from the product 
            product.name = remove_last_character(product.name)
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form})
