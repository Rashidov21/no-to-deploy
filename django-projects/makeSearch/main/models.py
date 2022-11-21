from django.db import models

# Create your models here.

# Country


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return str(self.name)

# Club


class Club(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)
# Player
# o.players = all players


class Player(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name='players_of_country')
    club = models.ForeignKey(
        Club, on_delete=models.PROTECT, related_name='players')
    age = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)


class ClubManager(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='managers/')
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT)
    club = models.ForeignKey(
        Club, on_delete=models.PROTECT)
    age = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.name)
