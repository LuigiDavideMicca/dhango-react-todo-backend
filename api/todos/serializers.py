import datetime
from rest_framework import serializers
from todos.models import Todo
from categories.models import Category
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'categories', 'todos', 'owner']

class TodosSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta: 
        model = Todo
        fields = ['id', 'title', 'text', 'category', 'done_by', 'owner']
