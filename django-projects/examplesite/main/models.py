from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
