from django.urls import path
from . import views

# 🌐 تعريف مساحة الأسماء الخاصة بالتطبيق
app_name = "core"

urlpatterns = [
    # 🏡 الصفحة الرئيسية
    path("", views.home, name="home"),

    # ✉️ صفحة "اتصل بنا"
    path("contact/", views.contact, name="contact"),
    # 🧭 صفحة من نحن / عنا
    path('about/', views.about, name='about'),
]
