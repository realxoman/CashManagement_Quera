from django.contrib import admin
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('password',)

    fieldsets = (
        ("Personal", {'fields': ('username', "password",
         'email', 'first_name', 'last_name',)}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ("Special Permission", {'fields': ("special_user_permission",)}),

    )

    add_fieldsets = (
        ("Personal", {'fields': ('username', "password",
         'email', 'first_name', 'last_name',)}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ("Special Permission", {'fields': ("special_user_permission",)}),

    )
