import pytest
from django.urls import reverse
from support.models import Message
from support.serializer import MessageSerializer
from django.contrib.auth.models import User

from rest_framework.test import APIClient

"""  Arrange  """


@pytest.fixture
def test_user(db):
    user = User.objects.create_user("admin")
    return user


@pytest.fixture
def api_client(test_user):
    client = APIClient()
    client.force_authenticate(test_user)
    return client


""" Act """


def test_post_message(api_client, test_user):
    url = reverse('message-list')
    payload = dict(
        title="New title",
        content="NEW content",
        sender=test_user
    )
    response = api_client.post(url, payload)
    """ Assert """
    assert response.status_code == 201


""" Act """


@pytest.mark.django_db
def test_list_message(api_client):
    url = reverse('message-list')
    response = api_client.get(url)
    messages = Message.objects.all()
    expected_data = MessageSerializer(messages, many=True).data
    """ Assert """
    assert response.status_code == 200
    assert response.data == expected_data
