from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),   # إدارة المستخدمين والتوثيق
    path('store/', include('store.urls')),         # المتجر والمنتجات والطلبات
    path('', include('core.urls')),                # الصفحات العامة والواجهة الرئيسية
]
