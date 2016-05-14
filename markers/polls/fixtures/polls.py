import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Poll
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def poll_factory(db, topic_factory):
    class PollFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Poll

        name = faker.sentence(nb_words=10)
        info = faker.sentence(nb_words=200)
        topic = factory.SubFactory(topic_factory)

    return PollFactory


@pytest.fixture
def sample_poll(poll_factory):
    '''
    sample usage:
    > poll1 = sample_poll()
    > poll2 = sample_poll()
    > Poll.objects.all().count() # returns 2
    '''

    def factory_worker(**custom_fields):
        defaults = {
            "name": factory.LazyAttribute(lambda x: faker.sentence(nb_words=5)),
            "info": factory.LazyAttribute(lambda x: faker.sentence(nb_words=200)),
        }
        defaults = extend(defaults, custom_fields)
        return poll_factory(**defaults)

    return factory_worker
