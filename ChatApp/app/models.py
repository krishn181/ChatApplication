from django.db import models
from django.contrib.auth.models import User
class Chat(models.Model):
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    
