from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category


# 🛍️ عرض جميع المنتجات في المتجر
def product_list(request):
    """
    🛍️ عرض جميع المنتجات في المتجر مع إمكانية تصفح التصنيفات
    """
    # ✅ جلب التصنيفات بالترتيب الأبجدي
    categories = Category.objects.all().order_by('name')

    # ✅ جلب جميع المنتجات مرتبة بالأحدث
    products = Product.objects.all().order_by('-created_at')

    # 🟡 في حال لم توجد منتجات في قاعدة البيانات
    if not products.exists():
        messages.info(request, "لا توجد منتجات حالياً في المتجر 🛒")

    # ✅ تمرير البيانات للقالب
    context = {
        "products": products,
        "categories": categories,
        "selected_category": None,
    }
    return render(request, "store-templates/product_list.html", context)


# 🧭 عرض المنتجات حسب التصنيف
def product_list_by_category(request, category_id):
    """
    🧭 عرض المنتجات بناءً على التصنيف الذي اختاره المستخدم
    """
    # 🔹 التأكد من وجود التصنيف المطلوب أو عرض 404
    category = get_object_or_404(Category, id=category_id)

    # 🔹 جلب المنتجات الخاصة بهذا التصنيف فقط
    products = Product.objects.filter(category=category).order_by('-created_at')

    # 🔹 جلب جميع التصنيفات لعرضها في الشريط الجانبي أو القائمة
    categories = Category.objects.all().order_by('name')

    # ⚠️ في حال عدم وجود منتجات ضمن هذا التصنيف
    if not products.exists():
        messages.warning(request, f"🚫 لا توجد منتجات حالياً ضمن تصنيف: {category.name}")

    # ✅ تمرير البيانات إلى القالب
    context = {
        "products": products,
        "categories": categories,
        "selected_category": category,
    }
    return render(request, "store-templates/product_list.html", context)


# 🛒 إضافة منتج إلى السلة
def add_to_cart(request, product_id):
    """
    🛒 إضافة منتج إلى السلة باستخدام الـ session
    """
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # 🔹 إذا المنتج موجود مسبقاً في السلة، زِد الكمية
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        # 🔹 إضافة المنتج الجديد للسلة
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    # 🔹 حفظ التحديث في الجلسة
    request.session['cart'] = cart

    messages.success(request, f"✅ تم إضافة {product.name} إلى السلة بنجاح 🛍️")
    return redirect('store:product_list')


# 🧾 عرض تفاصيل السلة
def cart_detail(request):
    """
    🧾 عرض السلة الخاصة بالمستخدم
    """
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    context = {
        'cart': cart,
        'total': round(total, 2),
    }
    return render(request, 'store-templates/cart_detail.html', context)
