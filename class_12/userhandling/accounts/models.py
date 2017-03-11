from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class MyUser(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, default='')
	address = models.CharField(max_length=300, default='')
	contact = models.CharField(max_length=12, null=True)

	def __unicode__(self):
		return self.user.username


class RegisterForm(forms.Form):
	name = forms.CharField(max_length=50, label='Your Name')
	username = forms.CharField(max_length=20, label='Username')
	password = forms.CharField(widget=forms.PasswordInput(), label='Password')
	address = forms.CharField(max_length=200, label='Your Address')
	contact = forms.CharField(max_length=12, label='You Contact')

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20, label='Username')
	password = forms.CharField(widget=forms.PasswordInput(), label='Password')