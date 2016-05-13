from rest_framework import serializers
from polls.models import Poll, PollChoice, PollResponse

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('name', 'info', 'topic')


class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PollChoice
		fields = ('poll', 'text')


class PollResponseSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	poll_choice = serializers.ReadOnlyField(source='poll_choice.text')

	class Meta:
		model = PollResponse
		fields = ('poll_choice', 'user')
	