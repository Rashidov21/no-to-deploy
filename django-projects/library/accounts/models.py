from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    GENDERS = (
        ("Men", "men"),
        ("Women", "women")
    )

    age = models.PositiveIntegerField(default=0, blank=True)
    gender = models.CharField(choices=GENDERS, blank=True, max_length=30)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to=f'users/', blank=True)

    def get_user_fullname(self):
        name = ""
        if self.first_name and self.last_name:
            name = f"{self.first_name.title()} {self.last_name.title()}"
        else:
            name = "No user full name"
        return name

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
