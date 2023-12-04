from django.db import models

from django.db import models
from django.urls import reverse

import django_filters

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse(
            "task-update", args=[self.id]
        )

    def __str__(self):  
        return self.title

    class Meta:
        ordering = ["title"]    
        
class TaskFilter(django_filters.FilterSet):
    class Meta:
        model: Task
        fields = {
            'title': ['exact', 'contains'], 
            'description': ['exact', 'contains'], 
            'created_date': ['exact']
        }