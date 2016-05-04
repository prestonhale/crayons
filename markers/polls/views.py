import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from polls.models import Poll

def polls(request):
	all_polls=Poll.objects.all()
	json_all_polls=serializers.serialize('json', all_polls)
	return HttpResponse(json_all_polls)