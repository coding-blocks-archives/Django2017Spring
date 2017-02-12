from __future__ import unicode_literals

from django.db import models



class UserData(models.Model):
	username = models.CharField(max_length=100, unique=True)
	user_key = models.CharField(max_length=100)

	def __unicode__(self):
		return self.username


class GameData(models.Model):
	user = models.ForeignKey(UserData)
	game_id = models.CharField(max_length=10, null=True)
	game_score = models.IntegerField(default=0)

	def __unicode__(self):
		try:
			return "GameID: " + self.game_id
		except:
			return "Empty GameID"