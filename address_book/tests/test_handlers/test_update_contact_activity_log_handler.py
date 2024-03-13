import pytest
from django.urls import reverse
from .test_config import api_client, contact_factory
from contacts.models import ContactActivityLog


@pytest.mark.django_db
def test_update_contact_activity_log(api_client, contact_factory):
    contact = contact_factory(first_name='John', city='New York')
    url = reverse('contact-detail', args=[contact.pk])

    updated_data = {'first_name': 'JohnUpdated', 'city': 'NY'}

    response = api_client.patch(url, updated_data, format='json')

    assert response.status_code == 200
    assert ContactActivityLog.objects.filter(
        contact=contact,
        activity_type='EDITED'
    ).exists()
