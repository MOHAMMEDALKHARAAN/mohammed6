from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 🟤 صفحة تسجيل الدخول
    path('login/', views.user_login, name='login'),

    # 🟤 صفحة إنشاء حساب جديد
    path('register/', views.user_register, name='register'),

    # 🟤 تسجيل الخروج
    path('logout/', views.user_logout, name='logout'),
]
