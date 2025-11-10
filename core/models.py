from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSetting(models.Model):
    """
    إعدادات الموقع العامة
    """
    site_name = models.CharField(max_length=100, default="متجري الإلكتروني", verbose_name=_("اسم الموقع"))
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name=_("شعار الموقع"))
    contact_email = models.EmailField(blank=True, null=True, verbose_name=_("البريد الإلكتروني"))
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("رقم التواصل"))
    footer_text = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("نص التذييل"))

    class Meta:
        verbose_name = _("إعداد الموقع")
        verbose_name_plural = _("إعدادات الموقع")

    def __str__(self):
        return self.site_name


class ContactMessage(models.Model):
    """
    رسائل "اتصل بنا"
    """
    name = models.CharField(max_length=100, verbose_name=_("الاسم"))
    email = models.EmailField(verbose_name=_("البريد الإلكتروني"))
    subject = models.CharField(max_length=150, verbose_name=_("الموضوع"))
    message = models.TextField(verbose_name=_("الرسالة"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإرسال"))
    is_read = models.BooleanField(default=False, verbose_name=_("تمت القراءة"))

    class Meta:
        verbose_name = _("رسالة")
        verbose_name_plural = _("الرسائل")

    def __str__(self):
        return f"{self.name} - {self.subject}"
