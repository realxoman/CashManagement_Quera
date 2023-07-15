from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import CustomUser


admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username',)
    readonly_fields = ('password',)

    fieldsets = (
        ("Personal", {'fields': ('username', "password", 'balance')}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )

    add_fieldsets = (
        ("Personal", {'fields': ('username', "password", 'balance')}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )
