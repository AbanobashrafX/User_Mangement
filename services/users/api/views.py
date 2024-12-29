from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..selectors import get_active_users, get_user_by_id, get_users
from ..services import delete_user, update_user
from .serializers import UserDetailSerializer, UserSerializer


class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        users = get_users()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


class UserCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # You might want to use the create_user service here for more control
        return Response(serializer.data)


class UserUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def put(self, request, uuid):
        user = get_user_by_id(uuid)
        if user is None:
            raise "Http404"

        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        update_user(user, **serializer.validated_data)
        return Response(serializer.data)


class UserDetailsView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserDetailSerializer

    def get(self, request, uuid):
        user = get_user_by_id(uuid)
        serializer = self.serializer_class(user)

        return Response(serializer.data)


class UserDeleteView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, uuid):
        user = get_user_by_id(uuid)
        if user is None:
            raise "Http404"

        delete_user(user)
        return Response(status=204)


class UserActivateListView(APIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = get_active_users()
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)
