from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MyUser(models.Model):
	name = models.CharField(max_length=200, default='')
	username = models.CharField(max_length=100, unique=True)
	games_played = models.IntegerField(default=0)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return 'User: ' + self.username


class Quiz(models.Model):
	name = models.CharField(max_length=200, default='')
	user = models.ForeignKey(MyUser, null=True)
	quiz_type = models.CharField(max_length=200, default='')
	score = models.IntegerField(default=0)
	questions = models.CharField(max_length=500, default='')

	def __unicode__(self):
		return 'Quiz: ' + self.name + ', for: ' + self.user.name


class Questions(models.Model):
	question = models.CharField(max_length=500, default='')

	def __unicode__(self):
		return 'Question: ' + self.question


class Answers(models.Model):
	option = models.CharField(max_length=200, default='')
	correct = models.BooleanField(default=False)
	question = models.ForeignKey(Questions)

	def __unicode__(self):
		return 'Answer: ' + self.option