import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Response
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def response_factory(db, user_factory, poll_choice_factory):
    class ResponseFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Response

        user = factory.SubFactory(user_factory)
        poll_choice = factory.SubFactory(poll_choice_factory)

    return ResponseFactory


@pytest.fixture
def sample_response(response_factory):
    '''
    sample usage:
    > response1 = sample_response()
    > response2 = sample_response()
    > Response.objects.all().count() # returns 2
    '''

    def factory_worker(**custom_fields):
        defaults = extend({}, custom_fields)
        return response_factory(**defaults)

    return factory_worker

