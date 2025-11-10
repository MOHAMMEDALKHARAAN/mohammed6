from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    """➕ إضافة منتج إلى السلة"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('store:cart_detail')


def cart_remove(request, product_id):
    """❌ إزالة منتج من السلة"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('store:cart_detail')


def cart_detail(request):
    """🧾 عرض تفاصيل السلة"""
    cart = Cart(request)
    return render(request, 'store-templates/cart_detail.html', {'cart': cart})
