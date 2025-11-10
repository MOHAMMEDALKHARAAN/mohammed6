from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    """
    عرض جميع المنتجات في المتجر
    """
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, "store-templates/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": None,
    })


def product_list_by_category(request, category_id):
    """
    عرض المنتجات بناءً على التصنيف المحدد
    """
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, "store-templates/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": category,
    })
