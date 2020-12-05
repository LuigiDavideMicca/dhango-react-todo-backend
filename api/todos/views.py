from todos.models import Todo
from todos.serializers import TodosSerializer, UserSerializer
from django.http import Http404
from rest_framework import generics, permissions, authentication
from django.contrib.auth.models import User


class TodosList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    serializer_class = TodosSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    authentication_classes = [authentication.TokenAuthentication]


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
         
    serializer_class = TodosSerializer


    permission_classes = [permissions.IsAuthenticated]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer