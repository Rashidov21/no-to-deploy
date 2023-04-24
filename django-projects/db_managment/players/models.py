from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='club_logos/%Y/%m/%d')

    def __str__(self):
        return str(self.name)


    

class Player(models.Model):
    
    POSITONS = (
        ('gk', "Goalkeeper"),
        ('df', "Deffender"),
        ('md', "Middle Deffender"),
        ('fw', "Forward"),
        ('st', "Striker"),
    )

    
    name = models.CharField(max_length=150)
    birthday = models.DateField(blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='players/%Y/%m/%d')    
    height = models.FloatField(blank=True)
    weight = models.FloatField(blank=True)
    country = models.CharField(max_length=150,blank=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name='players', null=True)
    position = models.CharField(choices=POSITONS,blank=True, max_length=50)
    current_price = models.FloatField(default=0,blank=True)
    
    def __str__(self):
        return str(self.name)


class PlayerImages(models.Model):
    image = models.ImageField(upload_to='players/%Y/%m/%d')
    player = models.ForeignKey(
        Player,
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='player_images')
    
    def __str__(self):
        return self.player.name

    class Meta:
        verbose_name = 'Player rasmlari'
        verbose_name_plural = 'Player rasmlari'