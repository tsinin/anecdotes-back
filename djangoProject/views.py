from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, permissions
from djangoProject.anecdotes.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
