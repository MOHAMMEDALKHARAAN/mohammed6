from django.shortcuts import render
from store.models import Product, Category

def home(request):
    """
    الصفحة الرئيسية للمتجر
    - تعرض البنر الرئيسي
    - تعرض أحدث المنتجات (حتى 6 منتجات)
    """
    # 🔹 جلب آخر 6 منتجات من قاعدة البيانات
    products = Product.objects.all().order_by('-created_at')[:6]

    # 🔹 جلب التصنيفات (في حال أردت عرضها لاحقًا)
    categories = Category.objects.all()

    # 🔹 تمرير البيانات إلى القالب
    context = {
        "products": products,
        "categories": categories,
        "selected_category": None,
    }

    return render(request, "home.html", context)
