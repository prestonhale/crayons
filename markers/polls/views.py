import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Poll, PollChoice, PollResponse, Topic
from polls.serializers import PollSerializer

# ========= Not used =========
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
	"""
	An HTTPResponse that renders its content to JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
# =============================


# We want to post to this view which won't provide a CSRF token.
# Replace this functionality in production build.
@api_view(['GET', 'POST'])
def poll_list(request, format=None):
	"""
	List all polls, or create a new poll.
	"""
	if request.method=="GET":
		polls = Poll.objects.all()
		serializer = PollSerializer(polls, many=True)
		return Response(serializer.data)

	elif request.method == "POST":
		serializer = PollSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def poll_detail(request, pk, format=None):
	"""
	Retrieve, update or delete a poll
	"""
	try:
		poll = Poll.objects.get(pk=pk)
	except Poll.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = PollSerializer(poll)
		return Response(serializer.data)

	# Update poll 
	elif request.method == "PUT":
		serializer = PollSerializer(poll, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == "DELETE":
		poll.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)