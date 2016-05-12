from rest_framework import serializers
from polls.models import Poll, LANGUAGE_CHOICES, STYLE_CHOICES

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('name', 'info', 'topic', 'language', 'style')
	