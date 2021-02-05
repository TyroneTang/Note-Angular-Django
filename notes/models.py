from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(null=True, max_length=60)
    note = models.TextField(null=False)
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE, related_name="notes")
    
    # created at and updated at
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str (self.title)
