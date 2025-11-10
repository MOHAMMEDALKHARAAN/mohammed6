from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from store.models import Product, Category
from .models import ContactMessage


def home(request):
    """
    🏠 الصفحة الرئيسية للمتجر
    ───────────────────────────────
    تعرض البنر الرئيسي وأحدث 6 منتجات مع التصنيفات.
    """
    try:
        # 🔹 جلب أحدث 6 منتجات فقط لتقليل الحمل
        products = Product.objects.select_related("category").order_by("-created_at")[:6]
        categories = Category.objects.all().order_by("name")

        context = {
            "products": products,
            "categories": categories,
            "selected_category": None,
        }

        return render(request, "home.html", context)

    except Exception as e:
        # 🧱 معالجة الخطأ وتسجيله في الطرفية
        print(f"❌ خطأ في تحميل الصفحة الرئيسية: {e}")
        messages.error(request, "حدث خطأ أثناء تحميل الصفحة. يرجى المحاولة لاحقًا.")
        return render(request, "home.html", {
            "products": [],
            "categories": [],
            "error_message": "حدث خطأ أثناء تحميل الصفحة.",
        })


def contact(request):
    """
    ✉️ صفحة "اتصل بنا"
    ───────────────────────────────
    تسمح للمستخدمين بإرسال رسالة إلى إدارة المتجر.
    """
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip() or "بدون عنوان"
        message = request.POST.get("message", "").strip()

        # ✅ التحقق من تعبئة الحقول
        if not name or not email or not message:
            messages.warning(request, "⚠️ يرجى تعبئة جميع الحقول المطلوبة.")
            return redirect("core:contact")

        # ✅ التحقق من صحة البريد الإلكتروني
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "❌ البريد الإلكتروني غير صالح.")
            return redirect("core:contact")

        # ✅ حفظ الرسالة في قاعدة البيانات
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            messages.success(request, "✅ تم إرسال رسالتك بنجاح! سنتواصل معك قريبًا.")
            return redirect("core:contact")

        except Exception as e:
            print(f"❌ خطأ أثناء حفظ الرسالة: {e}")
            messages.error(request, "حدث خطأ أثناء إرسال الرسالة. حاول مرة أخرى لاحقًا.")

    # 🔹 عرض صفحة الاتصال (GET)
    return render(request, "core-templates/contact.html")
def about(request):
    """
    🧭 صفحة "عنا"
    ───────────────────────────────
    تعرض نبذة عن المتجر ورؤيته ورسالة الفريق.
    """
    context = {
        "page_title": "عن متجر SH",
        "about_text": (
            "متجر SH هو وجهتك الأولى لعالم المنتجات الفاخرة والعصرية. "
            "نقدم لك تجربة تسوق إلكتروني تجمع بين الجودة العالية "
            "والتصميم الأنيق، مع التزامنا بخدمة عملاء متميزة واهتمام بأدق التفاصيل. "
            "نهدف إلى جعل كل منتج في متناولك تجربة استثنائية تعبّر عن ذوقك الرفيع."
        )
    }
    return render(request, "core-templates/about.html", context)
