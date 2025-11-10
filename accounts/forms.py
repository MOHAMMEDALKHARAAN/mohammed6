from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    نموذج مخصص لإنشاء المستخدم مع الحقول الإضافية (الجوال والعنوان)
    """
    phone = forms.CharField(
        max_length=20,
        required=False,
        label="رقم الجوال",
        widget=forms.TextInput(attrs={'placeholder': '05xxxxxxxx'})
    )
    address = forms.CharField(
        required=False,
        label="العنوان",
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'اكتب عنوانك بالتفصيل'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم',
            'email': 'البريد الإلكتروني',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }
