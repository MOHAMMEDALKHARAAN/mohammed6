from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    🗂️ تصنيف المنتجات
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("اسم التصنيف"))
    description = models.TextField(blank=True, null=True, verbose_name=_("الوصف"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإضافة"))

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    🛍️ المنتجات
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name=_("التصنيف")
    )
    name = models.CharField(max_length=150, verbose_name=_("اسم المنتج"))
    description = models.TextField(blank=True, null=True, verbose_name=_("الوصف"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("السعر"))
    stock = models.PositiveIntegerField(default=0, verbose_name=_("الكمية المتوفرة"))
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name=_("صورة المنتج"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإضافة"))

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    📦 الطلبات
    """
    STATUS_CHOICES = [
        ('pending', _("قيد المعالجة")),
        ('shipped', _("تم الشحن")),
        ('delivered', _("تم التسليم")),
        ('cancelled', _("ملغي")),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name=_("المستخدم")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("آخر تحديث"))
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_("الحالة")
    )

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class OrderItem(models.Model):
    """
    🧾 عناصر الطلب
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("الطلب")
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("المنتج"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("الكمية"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("السعر الفردي"))

    class Meta:
        verbose_name = _("عنصر طلب")
        verbose_name_plural = _("عناصر الطلب")
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    def total_price(self):
        return self.price * self.quantity
