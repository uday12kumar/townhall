from django.db import models


class Food(models.Model):
	email = models.CharField(max_length=50)
	fooditem = models.CharField(max_length=50)
	date = models.DateField()
	restaurant = models.CharField(max_length=50)
	comment = models.TextField(blank=True)
	cost = models.CharField(max_length=50)
	total_cost = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=50)
	fooditems = models.CharField(max_length=50)
	contact = models.CharField(max_length=50)

	def __unicode__(self):
		return self.restaurant_name