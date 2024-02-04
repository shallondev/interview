from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    question = models.TextField()
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=64, unique=False, null=True, blank=True)

    def __str__(self):
        return f"ID: {self.id} User: {self.user} Tag: {self.tag}"