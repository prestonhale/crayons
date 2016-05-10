import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from polls.models import Poll, PollChoice, Response


def response_handler(*args, **kwargs):
    body = args[0]["data"]
    if kwargs.get("developerMessage", None):
        body["developerMessage"] = kwargs.pop("developerMessage")

    if kwargs.get("userMessage", None):
        body["userMessage"] = kwargs.pop("userMessage")
        
    return JsonResponse(*args, **kwargs)


def save_instance(instance):
    try:
        instance.save()
    except:
        logging.exception("There was an error at the database level")


def polls(request):
    all_polls=Poll.objects.all()
    return response_handler({"data": all_polls})


def responses(request, poll_id):
    poll_responses=Response.objects.filter(poll_choice__poll_id=poll_id)
    return response_handler({"data": poll_responses})


def add_response(request, poll_id):
    poll_choice_id=request.POST.get('poll_choice_id', None)
    if poll_choice_id:
        poll_choice=PollChoice.objects.get(id=poll_choice_id)
        Response.objects.create(poll_choice=poll_choice, user=request.user)
        response_data = {"poll_choice": poll_choice, "user": request.user}
        response = Response(**response_data)
        save_instance(response)

        return response_handler({}, status=201, 
            developer_message="Success!",
            user_message="Nice choice!",
        )

    else:
        return JsonResponse({}, status=400,
            developer_message="poll_choice_id is a required post param",
            user_message="Select a choice!",
        )
            
