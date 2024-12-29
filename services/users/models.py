import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any custom fields here, e.g.,

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=20, blank=True, unique=True)
    password = models.CharField(max_length=255, blank=False)
    
    

    def __str__(self):
        return self.get_full_name() or self.username
