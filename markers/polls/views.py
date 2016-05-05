import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from polls.models import Poll, Response

def polls(request):
	all_polls=Poll.objects.all()
	json_all_polls=serializers.serialize('json', all_polls)
	return HttpResponse(json_all_polls)

def responses(request, poll_id):
	poll_responses=Response.objects.filter(poll_choice__poll_id=poll_id)
	json_poll_responses=serializers.serialize('json', poll_responses)
	return HttpResponse(json_poll_responses)