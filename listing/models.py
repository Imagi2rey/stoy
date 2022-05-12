from django.db import models

# Create your models here.

class Stock(models.Model):
	entity = models.CharField(max_length=15)

	def __str__(self):
		return self.entity;
