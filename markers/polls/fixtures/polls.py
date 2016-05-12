import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Poll

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

    def factory_worker():
        name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=200))
        return poll_factory(name=name)

    return factory_worker
