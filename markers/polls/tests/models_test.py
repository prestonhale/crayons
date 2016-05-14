import pytest
from django.contrib.auth import get_user_model

from polls.models import Topic, Poll, PollChoice, Response

User = get_user_model()

'''
NOTE: we probably don't even need these tests since they're really just testing the django
framework itself, but I think we should keep them for now to increase test coverage. 
'''

def assert_created(model, *fixtures):

    def test_handler(*fixtures):
        instance = fixtures[0]()
        assert model.objects.all()[0] == instance

    test_handler(*fixtures)

'''
Since pytest looks for functions that start with test_, we can also define tests with 
lambda functions, making these super repetitive tests DRY and more concise. Super cool!
'''

test_create_user = lambda sample_user : assert_created(User, sample_user)
test_create_topic = lambda sample_topic : assert_created(Topic, sample_topic)
test_create_poll = lambda sample_poll : assert_created(Poll, sample_poll)
test_create_pollchoice = lambda sample_poll_choice : assert_created(PollChoice, sample_poll_choice)
test_create_response = lambda sample_response : assert_created(Response, sample_response)
