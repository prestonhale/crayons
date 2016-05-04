from django.db import models

# Create your models here.
class Poll(models):
	poll_id=models.AutoField(primary_key=True)
	name=models.CharField()
	info=models.CharField()
	topic_id=models.ForeignKey(topic_id)


class Topics(models):
	topic_id=models.AutoField(primary_key=True)
	name=models.CharField()