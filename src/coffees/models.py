from django.db import models
from django.urls import reverse

class Coffee(models.Model):
	name			= models.CharField(max_length=120)
	roaster			= models.ForeignKey('roasters.Roaster', on_delete=models.CASCADE)
	# roaster			= models.CharField(max_length=120)
	roast_date		= models.DateField(blank=True)
	best_by_date	= models.DateField(blank=True)
	notes			= models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse("coffees:coffee-detail", kwargs={'id': self.id})