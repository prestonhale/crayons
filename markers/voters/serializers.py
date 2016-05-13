from rest_framework import serializers
from voters.models import Voter

class VoterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Voter
		# Includes fields from user
		depth = 1
		fields = (
				'user', 'phone', 'phone_key', 'phone_key_generated_at',
				'carrier', 'phone_validated'
				)
	