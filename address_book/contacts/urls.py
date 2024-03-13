from contacts.views import ContactViewSet, ContactGroupViewSet, EventsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
router.register('contact-group', ContactGroupViewSet, basename='contact_group')
router.register('contact-events', EventsViewSet, basename='contact_events')

urlpatterns = router.urls

# urlpatterns = [
#     path('', ContactList.as_view(), name='contact_list'),
#     path('create/', ContactCreate.as_view(), name='contact_create'),
#     path('<int:pk>/', ContactRetrieve.as_view(), name='contact_retrieve'),
#     path('<int:pk>/delete/', ContactDestroy.as_view(), name='contact_destroy'),
#     path('<int:pk>/update', ContactUpdate.as_view(), name='contact_update'),
#     # path('<int:pk>/', ContactDetail.as_view())
# ]
