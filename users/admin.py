from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_hr_manager', 'is_employee')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('is_hr_manager', 'is_employee')}),
    )