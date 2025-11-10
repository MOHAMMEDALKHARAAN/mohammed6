from django.db import models


class SiteSetting(models.Model):
    """
    إعدادات الموقع العامة (اسم المتجر، البريد، الشعار...).
    """
    site_name = models.CharField(max_length=100, default="متجري الإلكتروني")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    footer_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.site_name


class ContactMessage(models.Model):
    """
    رسائل العملاء من نموذج "اتصل بنا".
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
