from .models import User


def get_user_by_id(user_id):
    """
    Retrieves a user by their ID.
    """
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


def get_users(limit=None):
    """
    Retrieves a list of users.
    """
    queryset = User.objects.all()
    if limit:
        queryset = queryset[:limit]
    return queryset
