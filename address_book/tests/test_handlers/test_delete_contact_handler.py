import pytest
from django.urls import reverse

from contacts.models import Contact
from .test_config import api_client


@pytest.fixture
def new_contact():
    contact = Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="NY",
        street="Main street",
        url="https://example.com",
        phone="+1234567890",
        image=None
    )
    return contact


@pytest.fixture
def contact_delete_contact_mock(mocker):
    return mocker.patch('contacts.models.Contact.delete')


@pytest.mark.django_db
def test_delete_contact(api_client, new_contact, contact_delete_contact_mock):
    url = reverse('contact-detail', kwargs={'pk': new_contact.pk})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert contact_delete_contact_mock.called
    assert contact_delete_contact_mock.call_count == 1
