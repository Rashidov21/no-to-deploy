from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AdvUser(AbstractUser):
	is_activated = models.BooleanField(default=True, db_index=True,
	verbose_name='Aktivatsiya qilinganmi ?'
	)
	send_messages = models.BooleanField(default=True,
	verbose_name='Yangi komentlar haqida xabarnomalar beraylikmi ?'
	)
	class Meta(AbstractUser.Meta):
		pass


class EmailNews(models.Model):
	name = models.CharField('Name', max_length=150)
	email = models.EmailField('Email', max_length=150)
	date = models.DateTimeField('Date', auto_now_add=True)

	def get_name(self):
		return str(self.name)
		
	def __str__(self):
		return str(self.email)