import pytest
from contacts.serializers import ContactGroupSerializer

from contacts.models import ContactGroup, Contact


@pytest.fixture
def test_contact_group():
    group = ContactGroup.objects.create(name="Test Group")
    contact1 = Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="New York",
        street="123 Main St",
        url="http://example.com/john_doe",
        phone="123456789"
    )
    contact2 = Contact.objects.create(
        first_name="Jane",
        last_name="Smith",
        country="UK",
        city="London",
        street="456 Elm St",
        url="http://example.com/jane_smith",
        phone="987654321"
    )
    group.contacts.add(contact1, contact2)

    return group


@pytest.mark.django_db
def test_contact_group_serialization(test_contact_group):
    serializer = ContactGroupSerializer(test_contact_group)
    serialized_data = serializer.data

    # Перевірка наявності полів у серіалізованому об'єкті
    assert 'id' in serialized_data
    assert 'name' in serialized_data
    assert 'contacts' in serialized_data

    # Перевірка коректності серіалізації контактів
    assert len(serialized_data['contacts']) == test_contact_group.contacts.count()
    for contact_data, contact_obj in zip(serialized_data['contacts'], test_contact_group.contacts.all()):
        assert contact_data['first_name'] == contact_obj.first_name
        assert contact_data['last_name'] == contact_obj.last_name
        assert contact_data['country'] == contact_obj.country
        assert contact_data['city'] == contact_obj.city
        assert contact_data['street'] == contact_obj.street
        assert contact_data['url'] == contact_obj.url
        assert contact_data['phone'] == contact_obj.phone
