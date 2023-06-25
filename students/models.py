from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    profile_img_url = models.URLField(null=True)
    total_time = models.PositiveIntegerField(default=0)
    forget_pass_token = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
