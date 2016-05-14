import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Topic
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def topic_factory(db):
    class TopicFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Topic

        name = faker.sentence(nb_words=5)

    return TopicFactory


@pytest.fixture
def sample_topic(topic_factory):
    '''
    sample usage:
    > topic1 = sample_topic()
    > topic2 = sample_topic()
    > Topic.objects.all().count() # returns 2
    '''

    def factory_worker(**custom_fields):
        defaults = {"name": factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))}
        defaults = extend(defaults, custom_fields)
        return topic_factory(**defaults)

    return factory_worker
