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


@pytest.fixture
def sample_full_poll_data_no_responses(sample_topic, sample_poll, sample_poll_choice):
    topic = sample_topic(name="Wildlife")
    poll = sample_poll(name="New State Bird", topic=topic)
    first_poll_choice = sample_poll_choice(text="Pidgey", poll=poll)
    second_poll_choice = sample_poll_choice(text="A Porcupine", poll=poll)
    return poll

@pytest.fixture
def sample_full_poll_data_with_responses(sample_user, sample_full_poll_data_no_responses, sample_response):
    bob = sample_user(username="bob")
    tom = sample_user(username="tom")
    poll = sample_full_poll_data_no_responses
    poll_choices = poll.pollchoice_set.all()

    sample_response(poll_choice=poll_choices[0], user=bob)
    sample_response(poll_choice=poll_choices[1], user=tom)
    return poll
