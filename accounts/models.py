from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    نموذج المستخدم الأساسي (عميل أو مشرف)
    """
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("رقم الجوال")
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("العنوان")
    )

    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")

    def __str__(self):
        return self.username


class Address(models.Model):
    """
    عنوان الشحن المرتبط بالمستخدم
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addresses', verbose_name=_("المستخدم"))
    full_name = models.CharField(max_length=100, verbose_name=_("الاسم الكامل"))
    city = models.CharField(max_length=50, verbose_name=_("المدينة"))
    region = models.CharField(max_length=50, verbose_name=_("المنطقة"))
    details = models.TextField(blank=True, null=True, verbose_name=_("تفاصيل إضافية"))
    is_default = models.BooleanField(default=False, verbose_name=_("افتراضي"))

    class Meta:
        verbose_name = _("عنوان")
        verbose_name_plural = _("العناوين")

    def __str__(self):
        return f"{self.full_name} - {self.city}"
