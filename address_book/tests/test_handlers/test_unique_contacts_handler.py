import pytest
from django.db.utils import IntegrityError
from contacts.models import Contact


@pytest.mark.django_db
def test_create_duplicate_contact():
    Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="NY",
        street="Main street",
        url="https://example.com",
        phone="+1234567890",
        image=None
    )

    with pytest.raises(IntegrityError):
        Contact.objects.create(
            first_name="John",
            last_name="Doe",
            country="USA",
            city="NY",
            street="Main street",
            url="https://example.com",
            phone="+1234567890",
            image=None
        )
