from calendar import c
from re import U

from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from .models import User
from .services import create_user, update_user


@admin.register(User)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "is_admin",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("username", "email")
    list_filter = ("is_active", "is_admin", "is_superuser")

    fieldsets = (
        (
            "Account credentials",
            {
                "fields": (
                    "username",
                    "email",
                )
            },
        ),
        ("Booleans", {"fields": ("is_active", "is_admin", "is_superuser")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = ("username",)

    def save_model(self, request, obj, form, change):
        # if change:
        #     print("Updating user")
        #     try:
        #         update_user(obj, **form.cleaned_data)
        #         self.message_user(request, "User updated successfully.", messages.SUCCESS)
        #     except ValidationError as exc:
        #         self.message_user(request, str(exc), messages.ERROR)
        #     return super().save_model(request, obj, form, change)

        try:
            create_user(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
        else:
            self.message_user(request, "User created successfully.", messages.SUCCESS)
