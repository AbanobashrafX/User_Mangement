from .models import User


def create_user(username, password, **extra_fields):
    """
    Creates a new user with the given credentials.
    """
    user = User.objects.create_user(
        username=username, password=password, **extra_fields
    )
    return user


def update_user(user, **kwargs):
    """
    Updates an existing user with the given data.
    """
    for key, value in kwargs.items():
        setattr(user, key, value)
    user.save()
    return user


def delete_user(user):
    """
    Deletes a user.
    """
    user.delete()
