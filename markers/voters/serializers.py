from rest_framework import serializers
from voters.models import Voter, CellCarrier

class VoterSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	carrier = serializers.HyperlinkedRelatedField(
		view_name = 'carrier-detail',
		read_only = True
	)

	class Meta:
		model = Voter
		# Includes fields from user
		depth = 1
		fields = (
				'user', 'phone', 'phone_key', 'phone_key_generated_at',
				'carrier', 'phone_validated'
				)

class CellCarrierSerializer(serializers.ModelSerializer):
	class Meta:
		model = CellCarrier
		fields = ('name','sms_gateway')
	