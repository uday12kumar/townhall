from django.db import models


class Food(models.Model):
	name = models.CharField(max_length=50)
	fooditem = models.CharField(max_length=50)
	date = models.CharField(max_length=20)
	restaurant = models.CharField(max_length=50)
	comment = models.TextField(blank=True)

	def __unicode__(self):
		return self.name