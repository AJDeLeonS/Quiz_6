from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=15, blank=True, null=True)

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"

