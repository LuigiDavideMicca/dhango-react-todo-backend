from categories.models import Category
from rest_framework import serializers


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = ['id', 'title', 'owner']
