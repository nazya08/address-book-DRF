import pytest
from .test_config import api_client
from contacts.models import ContactGroup, Contact


@pytest.mark.django_db
def test_create_contact_group(api_client):
    group = ContactGroup.objects.create(name="Test Group")
    contact1 = Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="NY",
        street="Main street",
        url="https://example.com",
        phone="+1234567890",
        image=None
    )
    contact2 = Contact.objects.create(
        first_name="Jane",
        last_name="Doe",
        country="USA",
        city="LA",
        street="Oak street",
        url="https://example.com",
        phone="+1987654321",
        image=None
    )

    group.contacts.add(contact1, contact2)

    assert contact1 in group.contacts.all()
    assert contact2 in group.contacts.all()
    assert len(group.contacts.all()) == 2
    assert group.contacts.get(pk=1).first_name == "John"
    assert group.contacts.get(pk=2).city == "LA"
