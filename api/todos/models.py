from django.db import models
from categories.models import Category

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.ForeignKey(Category, to_field="title", related_name='todos', on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=100, blank=True, default='')
    done_by = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ['done_by']

    def __str__(self):
        return self.title    
