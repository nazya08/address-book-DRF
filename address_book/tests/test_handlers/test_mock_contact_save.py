import pytest
from django.urls import reverse
from .test_config import api_client


@pytest.fixture
def contact_method_save_mock(mocker):
    return mocker.patch('contacts.models.Contact.save')


@pytest.mark.django_db
def test_contact_save_mock(api_client, contact_method_save_mock):
    url = reverse('contact-list')
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'country': 'Canada',
        'city': 'Toronto',
        'street': 'Street',
        'url': 'https://example.com',
        'phone': '+9876543210',
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == 201

    assert contact_method_save_mock.called
    assert contact_method_save_mock.call_count == 1
