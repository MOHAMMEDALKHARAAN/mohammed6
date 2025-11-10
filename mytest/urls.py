from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🎛️ لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # 👥 روابط تطبيق إدارة المستخدمين والتوثيق
    path('accounts/', include('accounts.urls')),

    # 🛒 روابط تطبيق المتجر والمنتجات والطلبات
    path('store/', include('store.urls')),

    # 🌐 روابط التطبيق الأساسي (الصفحات العامة والواجهة الرئيسية)
    path('', include('core.urls')),
]


# 🖼️ عرض ملفات الوسائط والستايل أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
