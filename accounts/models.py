from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    نموذج المستخدم الأساسي (عميل أو مشرف).
    يمكن لاحقاً توسيعه لإضافة أدوار أو صلاحيات إضافية.
    """
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")

    def __str__(self):
        return self.username


class Address(models.Model):
    """
    عنوان شحن مرتبط بالمستخدم.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
