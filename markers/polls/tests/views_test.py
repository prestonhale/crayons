import pytest
from django.core.urlresolvers import resolve, reverse
from django.core import serializers

from polls.views import PollList, PollDetail, PollChoiceList, PollResponseList, PollResponseDetail
from polls.models import PollResponse


def assert_view_returned(urlname, view, **url_kwargs):

    def test_handler():
        url = reverse(urlname, **url_kwargs)
        found = resolve(url)
        assert found.func.__name__ == view.as_view().__name__

    test_handler()


test_polls_url = lambda: assert_view_returned('poll-list', PollList)
test_responses_url = lambda sample_poll: assert_view_returned('response-list', PollResponseList)
test_add_response_url = lambda sample_poll: assert_view_returned('response-list', PollResponseList)


@pytest.mark.integration
def test_poll_endpoint(rest_client, sample_user, sample_poll):
    user = sample_user()
    poll1 = sample_poll()
    poll2 = sample_poll()

    rest_client.force_authenticate(user=user)
    path = reverse('poll-list')
    response = rest_client.get(path).json()
    results = response.get("results", None)

    assert results
    assert len(results) == 2
    assert response.get("count", 0) == 2


'''
Need to figure out how to authenticate for the endpoint these tests call

@pytest.mark.integration
def test_responses_view_returns_all_possible_responses(sample_user, sample_full_poll_data_with_responses):
    user = sample_user()
    poll = sample_full_poll_data_with_responses

    client = APIClient()
    client.force_authenticate(user=user)
    path = reverse('response-list')
    response = client.get(path).json()
    print (response)
    results = response.get("results", None)
    print (results)

    assert results[0].object.user.username == 'bob'
    assert results[1].object.poll_choice.poll.name == 'New State Bird'


@pytest.mark.integration
def test_can_add_response_via_url(client, sample_user, sample_full_poll_data_no_responses):
    bob = sample_user(username="bob", password="orcpass")
    poll = sample_full_poll_data_no_responses
    first_poll_choice = poll.pollchoice_set.first()

    client.login(username='bob', password='orcpass')
    path = reverse('response-list')
    data={'poll_choice_id': first_poll_choice.id}
    client.post(path, data )
    
    responses = PollResponse.objects.all()
    assert responses.count() == 1
    response = responses.first()
    assert response.poll_choice.id == first_poll_choice.id
    assert response.user.id == bob.id
'''
