import pytest
from rest_framework.test import APIClient
from contacts.models import Contact, ContactGroup


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def contact_factory():
    def factory(first_name, city):
        return Contact.objects.create(first_name=first_name, city=city)
    return factory


@pytest.fixture
def contact_group_factory():
    def factory(name):
        return ContactGroup.objects.create(
            name=name,
        )
    return factory


@pytest.fixture
def contact():
    return Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="NY",
        street="Main street",
        url="https://example.com",
        phone="+1234567890",
        image=None  # можна додати зображення, якщо потрібно
    )


# @pytest.mark.django_db
# def test_filter_by_first_name(api_client, contact_factory):
#     contact_factory(first_name="John", city="NY")
#     contact_factory(first_name="Jane", city="LA")
#     url = reverse('contact-list')
#
#     response = api_client.get(url, {'first_name': 'John'})
#
#     assert response.status_code == 200
#     assert len(response.data) == 1
#     assert response.data[0]['first_name'] == "John"
#
#
# @pytest.mark.django_db
# def test_filter_by_city(api_client, contact_factory):
#     contact_factory(first_name="John", city="NY")
#     contact_factory(first_name="Jane", city="LA")
#     url = reverse('contact-list')
#
#     response = api_client.get(url, {'city': 'NY'})
#
#     assert response.status_code == 200
#     assert len(response.data) == 1
#     assert response.data[0]['city'] == "NY"
