from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
	author = models.CharField(max_length=200)
	name = models.CharField(max_length=500)
	summary = models.CharField(max_length=3000, default='')
	isbn = models.CharField(max_length=100, null=True)

	def __unicode__(self):
		return self.name

class News(models.Model):
	headline = models.CharField(max_length=500)
	source = models.CharField(max_length=500)
	points = models.IntegerField(null=True)
	author = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.headline