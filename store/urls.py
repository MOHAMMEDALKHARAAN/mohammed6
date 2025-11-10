from django.urls import path
from . import views
from . import views_cart  # ملف مخصص لإدارة السلة

app_name = 'store'

urlpatterns = [
    # 🛍️ عرض جميع المنتجات
    path('', views.product_list, name='product_list'),

    # 🧭 عرض المنتجات حسب التصنيف
    path('category/<int:category_id>/', views.product_list_by_category, name='product_by_category'),

    # 🛒 إدارة السلة (Cart Management)
    path('cart/', views_cart.cart_detail, name='cart_detail'),  # عرض محتوى السلة
    path('cart/add/<int:product_id>/', views_cart.cart_add, name='add_to_cart'),  # إضافة منتج
    path('cart/remove/<int:product_id>/', views_cart.cart_remove, name='cart_remove'),  # إزالة منتج
]
