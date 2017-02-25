from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.


class Book(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=500, default='')
	summary = models.CharField(max_length=3000, default='')
	isbn = models.CharField(max_length=100, null=True)
	url = models.CharField(max_length=400, null=True)

	def __unicode__(self):
		return self.name

class News(models.Model):
	headline = models.CharField(max_length=500)
	source = models.CharField(max_length=500)
	points = models.IntegerField(null=True)
	author = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.headline


class MyForm(forms.Form):
	name = forms.CharField(max_length=100, label='Your Name')
	address = forms.CharField(max_length=300, label='Your Address')
	phone = forms.CharField(max_length=15, label='Your Phone Number')
	age = forms.IntegerField(max_value=100, label='What is your age')