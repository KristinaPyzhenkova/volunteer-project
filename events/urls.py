from django.urls import path

from events.views import EventsListActive, EventsListProcess, EventsListClose
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsList, name='event_list'),
    path('active/', EventsListActive.as_view(), name='EventsListActive'),
    path('process/', EventsListProcess.as_view(), name='EventsListProcess'),
    path('closed/', EventsListClose.as_view(), name='EventsListClose'),
    path('<int:pk>/', views.EventDetail, name='event_detail'),
    path('<int:pk>/follow/', views.profile_follow, name='profile_follow'),
    path('<int:pk>/unfollow/', views.profile_unfollow, name='profile_unfollow'),
    path('<int:pk>/unfavorite/', views.profile_unfavorite, name='profile_unfavorite'),
    path('<int:pk>/favorite/', views.profile_favorite, name='profile_favorite'),
    path('<int:pk_event>/unfollow/<int:pk_funk>', views.profile_unfollow_func, name='profile_unfollow_func'),
    path('<int:pk_event>/follow/<int:pk_funk>', views.profile_follow_func, name='profile_follow_func'),
    path('follow/', views.follow_index, name='follow_index'),
    path('favorites/', views.favorites_index, name='favorites_index'),
    path('own/', views.own_index, name='own_index'),
    path('event_create/', views.event_create, name='event_create'),
    path('<int:pk>/function_create/', views.function_create, name='function_create'),
    path('<int:pk>/event_edit/', views.event_edit, name='event_edit'),
    path('<int:pk>/function_edit/', views.function_edit, name='function_edit'),

]
