from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Poll(models.Model):
    name=models.CharField(max_length=255)
    info=models.TextField()
    topic=models.ForeignKey(Topic)


class PollChoice(models.Model):
    poll=models.ForeignKey(Poll)
    text=models.TextField()


class Response(models.Model):
    poll_choice=models.ForeignKey(PollChoice)
    user=models.ForeignKey(User)
