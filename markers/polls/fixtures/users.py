import pytest
import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def user_factory(poll_factory):
    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = 'markers.User'

        email = faker.email()
        username = faker.user_name()
        password = factory.PostGenerationMethodCall('set_password', faker.password())

    return UserFactory


@pytest.fixture
def sample_user():
    '''
    sample usage:
    > user1 = sample_user()
    > user2 = sample_user()
    > User.objects.all().count() # returns 2
    '''

    email = factory.LazyAttribute(lambda x: faker.email())
    username = factory.LazyAttribute(lambda x: faker.user_name())
    password = factory.LazyAttribute(lambda x: faker.password())
    return user_factory()(email=email, username=username, password=password)

