from django.shortcuts import render
from store.models import Product, Category


def home(request):
    """
    🏠 الصفحة الرئيسية للمتجر
    - تعرض البنر الرئيسي.
    - تعرض أحدث المنتجات (حتى 6 منتجات فقط).
    - تمرر التصنيفات لاستخدامها في القوالب.
    """
    try:
        # 🔹 جلب أحدث 6 منتجات فقط لتخفيف الحمل على قاعدة البيانات
        products = Product.objects.select_related("category").order_by("-created_at")[:6]

        # 🔹 جلب جميع التصنيفات
        categories = Category.objects.all().order_by("name")

        # 🔹 تمرير البيانات إلى القالب
        context = {
            "products": products,
            "categories": categories,
            "selected_category": None,
        }

        return render(request, "home.html", context)

    except Exception as e:
        # 🧱 معالجة أي خطأ غير متوقع مع تسجيله في وحدة التحكم
        print(f"❌ خطأ في تحميل الصفحة الرئيسية: {e}")
        return render(request, "home.html", {
            "products": [],
            "categories": [],
            "error_message": "حدث خطأ أثناء تحميل الصفحة. يرجى المحاولة لاحقًا.",
        })
