from django.urls import path

from events.views import EventDetail, EventsList

app_name = 'events'

urlpatterns = [
    path('', EventsList.as_view(), name='event_list'),
    path('<int:pk>/', EventDetail.as_view(), name='event_detail'),
]
