from django.db import models


# Create your models here.

class News(models.Model):

	title = models.CharField('Title', max_length=150)
	body = models.TextField('Body', )
	date = models.DateTimeField('Published', auto_now_add=True)
	views = models.PositiveIntegerField('Views', default=0)

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name='News'
		verbose_name_plural='Newses'
		ordering = ['-date']


