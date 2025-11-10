from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🎛️ لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # 👥 تطبيق إدارة المستخدمين والتوثيق
    path('accounts/', include('accounts.urls')),

    # 🛒 تطبيق المتجر والمنتجات والطلبات
    path('store/', include('store.urls')),

    # 🌐 التطبيق الأساسي (الصفحات العامة والواجهة الرئيسية)
    path('', include('core.urls')),
]


# 🖼️ عرض ملفات الوسائط والستايل أثناء التطوير فقط (عند DEBUG=True)
if settings.DEBUG:
    # لعرض صور المستخدمين والمنتجات من مجلد media/
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # لعرض ملفات CSS/JS أثناء التطوير من مجلد static/
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
