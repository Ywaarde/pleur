from django.db import models
from django.urls import reverse

# Create your models here.
class Coffee(models.Model):
	name			= models.CharField(max_length=120)
	roaster			= models.TextField()
	roast_date		= models.DateField(blank=True)
	best_by_date	= models.DateField(blank=True)
	notes			= models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse("coffees:coffee-detail", kwargs={'id': self.id})