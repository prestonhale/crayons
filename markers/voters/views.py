from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from voters.models import Voter, CellCarrier
from voters import phone_validation
from datetime import datetime

# Create your views here.
def create_voter(request):
	user=User.objects.create_user(
		username=request.POST['username'],
		password=request.POST['password']
		)
	Voter.objects.create(
		user=user,
		phone=request.POST['phone'],
		carrier=CellCarrier.objects.get(id=request.POST['carrier']),
		)
	return HttpResponse(status=200)

def validate_phone(request):
	user=User.objects.get(id=request.POST['user_id'])
	voter=Voter.objects.get(user=user)

	key = phone_validation.send_text(voter)

	voter.phone_key = key
	voter.phone_key_generated = datetime.now()
	voter.save()

	return HttpResponse(status=200)