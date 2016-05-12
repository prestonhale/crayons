import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Response

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def response_factory(user_factory, poll_choice_factory):
    class ResponseFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Response

        user = factory.SubFactory(user_factory)
        poll_choice = factory.SubFactory(poll_choice_factory)

    return ResponseFactory


@pytest.fixture
def sample_response():
    '''
    sample usage:
    > response1 = sample_response()
    > response2 = sample_response()
    > Response.objects.all().count() # returns 2
    '''

    return response_factory()()
