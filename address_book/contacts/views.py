import django_filters

from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, permissions, filters

from contacts.models import Contact, ContactGroup, Events
from contacts.serializers import ContactSerializer, ContactGroupSerializer, EventsSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView


class ContactFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = ['first_name', 'city']


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ContactFilter
    search_fields = ['first_name', 'last_name', 'city', 'country', 'street']
    permission_classes = [permissions.AllowAny]


class ContactGroupViewSet(ModelViewSet):
    queryset = ContactGroup.objects.all()
    serializer_class = ContactGroupSerializer


class EventsViewSet(ModelViewSet):
    queryset = Events.objects.prefetch_related('contacts').all()
    serializer_class = EventsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location']

# class ContactList(ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['first_name', 'last_name', 'city']
#     permission_classes = [IsAuthenticated]
#
#
# class ContactRetrieve(RetrieveAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactUpdate(UpdateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactDestroy(DestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactCreate(CreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

#     def get(self, request, format=None):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ContactDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         contact = self.get_object(pk=pk)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         contact = self.get_object(pk=pk)
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         contact = self.get_object(pk=pk)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
