import pytest
import factory
from faker import Factory as FakerFactory
from django.contrib.auth import get_user_model

from utils.helpers import extend

User = get_user_model()

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def user_factory(db, poll_factory):
    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = User

        email = faker.email()
        username = faker.user_name()
        password = factory.PostGenerationMethodCall('set_password', faker.password())

    return UserFactory


@pytest.fixture
def sample_user(user_factory):
    '''
    sample usage:
    > user1 = sample_user()
    > user2 = sample_user()
    > User.objects.all().count() # returns 2
    '''

    def factory_worker(**custom_fields):
        defaults = {
            "email": factory.LazyAttribute(lambda x: faker.email()),
            "username": factory.LazyAttribute(lambda x: faker.user_name()),
            "password": factory.LazyAttribute(lambda x: faker.password()),
        }
        defaults = extend(defaults, custom_fields)

        return user_factory(**defaults)

    return factory_worker
