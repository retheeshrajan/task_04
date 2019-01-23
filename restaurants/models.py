from django.db import models

# Create your models here.
class Restaurant(models.Model):
	"""docstring for ClassName"""

	name=models.CharField(max_length=30)
	description=models.TextField()
	opening_time=models.CharField(max_length=30)
	closing_time=models.CharField(max_length=30)

	def __str__(self):
		return self.name

