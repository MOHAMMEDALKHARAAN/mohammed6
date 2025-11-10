from django.contrib import admin
from .models import User, Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)
    fieldsets = (
        ('معلومات الحساب', {'fields': ('username', 'email', 'password')}),
        ('معلومات شخصية', {'fields': ('first_name', 'last_name', 'phone', 'address')}),
        ('الصلاحيات', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تواريخ', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'region', 'is_default')
    list_filter = ('city', 'region', 'is_default')
    search_fields = ('full_name', 'city', 'region', 'user__username')
