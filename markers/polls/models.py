from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Pygment data
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Topic(models.Model):
	name=models.CharField(max_length=255)


class Poll(models.Model):
	name=models.CharField(max_length=255)
	info=models.TextField()
	topic=models.ForeignKey(Topic)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='python', max_length=100)


class PollChoice(models.Model):
	poll=models.ForeignKey(Poll)
	text=models.TextField()


class PollResponse(models.Model):
	poll_choice=models.ForeignKey(PollChoice)
	user=models.ForeignKey(User)