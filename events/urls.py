from django.urls import path

from events.views import EventsList
from . import views

app_name = 'events'

urlpatterns = [
    path('', EventsList.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetail, name='event_detail'),
    path('<int:pk>/follow/', views.profile_follow, name='profile_follow'),
    path('<int:pk>/unfollow/', views.profile_unfollow, name='profile_unfollow'),
    path('<int:pk>/unfavorite/', views.profile_unfavorite, name='profile_unfavorite'),
    path('<int:pk>/favorite/', views.profile_favorite, name='profile_favorite'),
    path('follow/', views.follow_index, name='follow_index'),
    path('favorites/', views.favorites_index, name='favorites_index'),
    path('event_create/', views.event_create, name='event_create'),
    path('<int:pk>/event_edit/', views.event_edit, name='event_edit'),

]
