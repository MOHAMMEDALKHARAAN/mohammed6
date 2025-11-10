from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # 🟤 عرض جميع المنتجات
    path('', views.product_list, name='product_list'),

    # 🟤 فلترة المنتجات حسب التصنيف
    path('category/<int:category_id>/', views.product_list_by_category, name='product_by_category'),
]
