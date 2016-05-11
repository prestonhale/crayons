import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Topic

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def topic_factory():
    class TopicFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Topic
                django_get_or_create = ('name',)

        name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))

    return TopicFactory
