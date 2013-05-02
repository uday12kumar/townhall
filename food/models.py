from django.db import models

class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=50)
	fooditems = models.TextField()
	contact = models.CharField(max_length=50)

	def __unicode__(self):
		return self.restaurant_name


class Order(models.Model):
    restaurant_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fooditem = models.TextField()
    date = models.DateTimeField()
    comment = models.TextField(blank=True)
    cost = models.IntegerField(max_length=5)
    total_cost = models.IntegerField(max_length=5)
    
    def __unicode__(self):
        return "Resturant: %s  --- %s" %(self.restaurant_name, self.fooditem)

