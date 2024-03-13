import pytest
from django.urls import reverse
from .test_config import api_client, contact_factory
from contacts.models import ContactActivityLog


@pytest.mark.django_db
def test_create_contact_activity_log(api_client, contact_factory):
    url = reverse('contact-list')
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'country': 'USA',
        'city': 'New York',
        'street': '123 Main St',
        'url': 'http://example.com/johndoe',
        'phone': '123-456-7890',
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == 201
    assert ContactActivityLog.objects.filter(
        contact__first_name=data['first_name'],
        contact__last_name=data['last_name'],
        activity_type='CREATED'
    ).exists()
