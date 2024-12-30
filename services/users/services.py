from django.contrib.auth.hashers import make_password

from .models import User


def create_user(username, password, **extra_fields):
    """
    Creates a new user with the given credentials.
    """
    data = {"username": username, "password": make_password(password)}
    user = User.objects.create_user(**data, **extra_fields)
    return user


def update_user(user, **kwargs):
    """
    Updates an existing user with the given data.
    """
    password = kwargs.pop("password", None)
    for key, value in kwargs.items():
        setattr(user, key, value)
    if password:
        user.set_password(make_password(password))
    user.save()
    return user


def delete_user(user):
    """
    Deletes a user.
    """
    user.delete()


def get_user_by_username(username):
    """
    Retrieves a user by their username.
    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def activate_user(user):
    """
    Activates a user account.
    """
    if not user.is_active:
        user.is_active = True
        user.save()


def deactivate_user(user):
    """
    Deactivates a user account.
    """
    if user.is_active:
        user.is_active = False
        user.save()


def set_password(user, new_password):
    """
    Sets a new password for the user.
    """
    user.password = make_password(new_password)
    user.save()
