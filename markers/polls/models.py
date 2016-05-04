from django.db import models

# Create your models here.
class Topic(models.Model):
	name=models.CharField(max_length=255)


class Poll(models.Model):
	name=models.CharField(max_length=255)
	info=models.TextField()
	topic=models.ForeignKey(Topic)