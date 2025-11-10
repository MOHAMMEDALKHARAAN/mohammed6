from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def user_login(request):
    """
    صفحة تسجيل الدخول
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"مرحباً {user.username} 👋 تم تسجيل الدخول بنجاح.")
                return redirect("/")
            else:
                messages.error(request, "بيانات الدخول غير صحيحة ❌")
        else:
            messages.error(request, "تحقق من البيانات المدخلة.")
    else:
        form = AuthenticationForm()

    return render(request, "account-templates/login.html", {"form": form})


def user_register(request):
    """
    صفحة إنشاء حساب جديد (مع الحقول الإضافية: الجوال والعنوان)
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 🔹 تسجيل المستخدم تلقائيًا بعد إنشاء الحساب
            login(request, user)
            messages.success(request, f"تم إنشاء الحساب بنجاح 🎉 أهلاً {user.username}")
            return redirect("/")
        else:
            messages.error(request, "تحقق من الحقول وأعد المحاولة.")
    else:
        form = CustomUserCreationForm()

    return render(request, "account-templates/register.html", {"form": form})


def user_logout(request):
    """
    تسجيل الخروج من الجلسة الحالية
    """
    logout(request)
    messages.success(request, "تم تسجيل الخروج بنجاح 👋")
    return redirect("/")
