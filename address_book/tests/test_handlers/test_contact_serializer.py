import pytest

from contacts.models import Contact
from contacts.serializers import ContactSerializer


@pytest.fixture
def expected_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "city": "New York",
        "street": "123 Main St",
        "url": "http://example.com/johndoe",
        "phone": "123-456-7890",
        "image": None
    }


@pytest.mark.django_db
def test_contact_serializer(expected_data):
    contact = Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="New York",
        street="123 Main St",
        url="http://example.com/johndoe",
        phone="123-456-7890",
        image=None
    )
    serializer = ContactSerializer(contact)

    assert serializer.data == expected_data
    assert len(serializer.data) == 8
