from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from contacts.models import Contact, ContactGroup, Events


class ContactSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    street = serializers.CharField(max_length=30)
    url = serializers.URLField(max_length=200)
    phone = serializers.CharField(max_length=30)
    image = serializers.ImageField(required=False)  # це поле не обов'язкове

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'country', 'city', 'street', 'url', 'phone', 'image']
#
#
# class ContactGroupSerializer(serializers.ModelSerializer):
#     contacts = ContactSerializer(many=True)
#
#     class Meta:
#         model = ContactGroup
#         fields = ['id', 'name', 'contacts']

# class ContactSerializer(serializers.ModelSerializer):
#     city = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=Contact.objects.all())])
#
#     def validate_city(self, value):
#         if any(char.isdigit() for char in value):
#             raise serializers.ValidationError('City cannot have a number')
#         return value
#
#     class Meta:
#         model = Contact
#         fields = '__all__'


class ContactGroupSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, required=False)

    class Meta:
        model = ContactGroup
        fields = '__all__'


class EventsSerializer(ContactGroupSerializer):
    title = serializers.CharField(max_length=40, validators=[UniqueValidator(queryset=Events.objects.all())])
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = '__all__'

    def get_contacts(self, obj):
        contacts_info = obj.contacts.all()
        return [{'id': contact.id, 'first_name': contact.first_name, 'last_name': contact.last_name} for contact in
                contacts_info]
