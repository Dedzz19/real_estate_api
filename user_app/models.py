from django.db import models
from django.contrib.auth.models import AbstractUser,User



class Agent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
      return self.name
