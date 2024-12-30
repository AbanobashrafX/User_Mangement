import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin

from services.common.models import BaseModel, models


class User(BaseModel, AbstractUser, PermissionsMixin):
    # Add any custom fields here, e.g.,

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=20, blank=True, unique=True)
    password = models.CharField(max_length=255, blank=False)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username
