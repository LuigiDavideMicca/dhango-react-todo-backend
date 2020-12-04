from django.db import models


class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='', unique=True)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return self.title    
