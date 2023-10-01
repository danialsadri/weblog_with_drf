from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


def get_user_photo(instance, filename):
    return f"user_photos/{instance.username}/{datetime.now().strftime('%Y/%m/%d')}/{filename}"


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    biography = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to=get_user_photo, blank=True, null=True)
