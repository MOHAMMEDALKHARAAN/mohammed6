from django.shortcuts import render
from .models import Product

def product_list(request):
    """
    عرض جميع المنتجات في المتجر
    """
    products = Product.objects.all().order_by('-created_at')
    return render(request, "store-templates/product_list.html", {"products": products})
