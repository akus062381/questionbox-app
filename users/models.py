from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")
    current_city = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=1000, null=True)


