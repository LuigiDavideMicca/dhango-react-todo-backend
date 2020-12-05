from categories.models import Category
from categories.serializers import CategoriesSerializer
from rest_framework import generics, permissions


class CategoriesList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    def get_queryset(self):
        owner = self.request.user
    
        return Category.objects.filter(owner=owner)


    serializer_class = CategoriesSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_queryset(self):
        owner = self.request.user
    
        return Category.objects.filter(owner=owner)

    serializer_class = CategoriesSerializer

    permission_classes = [permissions.IsAuthenticated]
