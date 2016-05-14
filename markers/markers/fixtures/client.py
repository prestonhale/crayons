import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture
def rest_client():
    return APIClient()


@pytest.fixture
def rest_factory():
    return APIRequestFactory()
