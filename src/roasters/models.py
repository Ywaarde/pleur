from django.db import models
from django.urls import reverse

class Roaster(models.Model):
	name	= models.CharField(max_length=120)
	city	= models.CharField(max_length=120)
	country	= models.CharField(max_length=120)
	website	= models.CharField(max_length=120)

	def get_absolute_url(self):
		return reverse("roasters:roaster-detail", kwargs={'id': self.id})
		
	def __str__(self):
		return self.name