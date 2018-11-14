from django.contrib.auth import get_user_model
from rest_framework import generics

from ..serializers import UserDetailSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailView(generics.RetrieveAPIView):
    queyryset = User.objects.all()
    serializer_class = UserDetailSerializer
