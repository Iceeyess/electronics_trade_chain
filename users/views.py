from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from users.models import User
from .apps import UsersConfig
from .permissions import IsActive
from .serializers import UserSerializer

app_name = UsersConfig.name

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     """Depends which action method returns list of permission classes"""
    #     if self.action == 'create':
    #         permission_classes = [AllowAny, ]
    #     elif self.action in ('retrieve', 'update', 'destroy', 'partial_update', 'list'):
    #         permission_classes = [IsActive, ]
    #     return [permission() for permission in permission_classes]