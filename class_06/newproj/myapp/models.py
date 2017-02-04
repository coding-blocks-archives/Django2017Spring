from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MyData(models.Model):
	name = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	organization = models.CharField(max_length=100, null=True)