import pytest
from django.core.urlresolvers import resolve, reverse
from django.core import serializers

from polls.views import polls, responses, add_response
from polls.models import Response


def assert_view_returned(url, view, **url_kwargs):

    def test_handler():
        if len(url_kwargs):
            print (url_kwargs)
            found = resolve(url.format(**url_kwargs))
        else:
            found = resolve(url)

        assert found.func == view

    test_handler()


test_polls_url = lambda: assert_view_returned('/polls/', polls)
test_responses_url = lambda sample_poll: assert_view_returned('/polls/{poll}/', responses,
        poll=sample_poll().id)
test_add_response_url = lambda sample_poll: assert_view_returned('/polls/{poll}/add/', add_response,
        poll=sample_poll().id)


@pytest.mark.integration
def test_poll_endpoint(client, sample_poll):
    poll1 = sample_poll()
    poll2 = sample_poll()
    path = reverse('polls')
    response = client.get(path)
    deserialized_objs = list(serializers.deserialize('json', response.content))
    assert len(deserialized_objs) == 2


@pytest.mark.integration
def test_responses_view_returns_all_possible_responses(client, sample_full_poll_data_with_responses):
    poll = sample_full_poll_data_with_responses
    path = reverse('responses', args=(poll.id,))
    response = client.get(path)
    deserialized_objs = list(serializers.deserialize('json', response.content))
    assert deserialized_objs[0].object.user.username == 'bob'
    assert deserialized_objs[1].object.poll_choice.poll.name == 'New State Bird'


@pytest.mark.integration
def test_can_add_response_via_url(client, sample_user, sample_full_poll_data_no_responses):
    bob = sample_user(username="bob", password="orcpass")
    poll = sample_full_poll_data_no_responses
    first_poll_choice = poll.pollchoice_set.first()

    client.login(username='bob', password='orcpass')
    path = reverse('add_response', args=(poll.id,))
    data={'poll_choice_id': first_poll_choice.id}
    client.post(path, data )
    
    responses = Response.objects.all()
    assert responses.count() == 1
    response = responses.first()
    assert response.poll_choice.id == first_poll_choice.id
    assert response.user.id == bob.id

