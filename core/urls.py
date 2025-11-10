from django.urls import path
from . import views

# 🏠 تطبيق الصفحات العامة (core)
app_name = 'core'

urlpatterns = [
    # 🔹 الصفحة الرئيسية للمتجر
    path('', views.home, name='home'),
]
