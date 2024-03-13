import pytest
from django.urls import reverse
from .test_config import api_client


@pytest.fixture
def contact_activity_log_create_mock(mocker):
    return mocker.patch('contacts.models.ContactActivityLog.objects.create')


@pytest.mark.django_db
def test_contact_activity_log_create_mock(api_client, contact, contact_activity_log_create_mock):
    url = reverse('contact-detail', kwargs={'pk': contact.pk})
    updated_data = {
        'first_name': 'UpdatedJohn',
        'last_name': 'UpdatedDoe',
        'country': 'Canada',
        'city': 'Toronto',
        'street': 'UpdatedStreet',
        'url': 'https://updated-example.com',
        'phone': '+9876543210',
    }

    response = api_client.put(url, updated_data, format='json')

    assert response.status_code == 200

    contact.refresh_from_db()
    assert contact.first_name == updated_data['first_name']
    assert contact.last_name == updated_data['last_name']
    assert contact.country == updated_data['country']
    assert contact.city == updated_data['city']
    assert contact.street == updated_data['street']
    assert contact.url == updated_data['url']
    assert contact.phone == updated_data['phone']

    expected_details = {
        'first_name': ('John', 'UpdatedJohn'),
        'last_name': ('Doe', 'UpdatedDoe'),
        'country': ('USA', 'Canada'),
        'city': ('NY', 'Toronto'),
        'street': ('Main street', 'UpdatedStreet'),
        'url': ('https://example.com', 'https://updated-example.com'),
        'phone': ('+1234567890', '+9876543210'),
    }

    actual_details = contact_activity_log_create_mock.call_args.kwargs['details']

    for field, (old_value, new_value) in expected_details.items():
        assert f'{field}: {old_value} -> {new_value}' in actual_details

    contact_activity_log_create_mock.assert_called_once_with(
        contact=contact,
        activity_type='EDITED',
        details=actual_details
    )
