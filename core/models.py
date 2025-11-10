from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSetting(models.Model):
    """
    ⚙️ إعدادات الموقع العامة
    ───────────────────────────────
    تحتوي على معلومات المتجر الأساسية مثل:
    - الاسم والشعار والعنوان.
    - بيانات التواصل (الهاتف والبريد الإلكتروني).
    - نص التذييل في أسفل الموقع.
    """

    site_name = models.CharField(
        max_length=100,
        default="متجري الإلكتروني",
        verbose_name=_("اسم الموقع"),
        help_text=_("اسم المتجر الذي سيظهر في الترويسة والتذييل."),
    )

    logo = models.ImageField(
        upload_to="logos/",
        blank=True,
        null=True,
        verbose_name=_("شعار الموقع"),
        help_text=_("يمكنك رفع الشعار الرسمي للمتجر."),
    )

    contact_email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_("البريد الإلكتروني"),
        help_text=_("البريد الإلكتروني الرسمي للتواصل."),
    )

    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("رقم التواصل"),
        help_text=_("رقم الهاتف أو الواتساب الخاص بالمتجر."),
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("العنوان"),
        help_text=_("عنوان المتجر أو مقر الإدارة."),
    )

    footer_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("نص التذييل"),
        help_text=_("نص يظهر أسفل الموقع، مثل حقوق النشر أو رسالة قصيرة."),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("آخر تعديل"),
    )

    class Meta:
        verbose_name = _("إعداد الموقع")
        verbose_name_plural = _("إعدادات الموقع")
        ordering = ["-updated_at"]

    def __str__(self):
        """عرض الاسم في لوحة الإدارة."""
        return self.site_name

    def __repr__(self):
        return f"<SiteSetting: {self.site_name}>"

    def get_logo_url(self):
        """
        🔗 إرجاع رابط الشعار (Logo) إن وجد،
        أو صورة افتراضية من مجلد static.
        """
        return self.logo.url if self.logo else "/static/images/default-logo.png"

    def get_contact_info(self):
        """
        🧭 إرجاع بيانات التواصل بشكل منسق.
        مفيدة للاستخدام في القوالب أو الـ API.
        """
        return {
            "email": self.contact_email or "غير متوفر",
            "phone": self.contact_phone or "غير متوفر",
            "address": self.address or "غير محدد",
        }


class ContactMessage(models.Model):
    """
    💬 نموذج (اتصل بنا)
    ───────────────────────────────
    لتخزين الرسائل المرسلة من نموذج التواصل في الموقع.
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("الاسم"),
        help_text=_("أدخل اسمك الكامل."),
    )

    email = models.EmailField(
        verbose_name=_("البريد الإلكتروني"),
        help_text=_("أدخل بريدك الإلكتروني للرد على استفسارك."),
    )

    subject = models.CharField(
        max_length=150,
        verbose_name=_("الموضوع"),
        blank=True,
        null=True,
        help_text=_("موضوع الرسالة (اختياري)."),
    )

    message = models.TextField(
        verbose_name=_("الرسالة"),
        help_text=_("اكتب تفاصيل رسالتك أو استفسارك."),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإرسال"),
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name=_("تمت القراءة"),
    )

    class Meta:
        verbose_name = _("رسالة")
        verbose_name_plural = _("الرسائل")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'بدون عنوان'}"

    def __repr__(self):
        return f"<ContactMessage from {self.name} ({self.email})>"
