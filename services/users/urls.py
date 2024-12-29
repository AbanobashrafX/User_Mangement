from django.urls import include, path, register_converter
from django.urls.converters import UUIDConverter
from rest_framework.routers import DefaultRouter

from .api.views import (
    UserCreateView,
    UserDeleteView,
    UserDetailsView,
    UserListView,
    UserUpdateView,
)

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("user/<uuid:uuid>/", UserDetailsView.as_view(), name="user-detail"),
    path("user/<uuid:uuid>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<uuid:uuid>/delete/", UserDeleteView.as_view(), name="user-delete"),
]
