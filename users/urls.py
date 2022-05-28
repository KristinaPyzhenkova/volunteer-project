from django.urls import path

from .views import UserListView, UserDetailView, EventListView, CertificateListView, ReviewListView, UserEdit

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(template_name='users/volunteers.html'), name='volunteers'),
    path('<int:pk>/', UserDetailView.as_view(template_name='users/volunteer_detail.html'), name='volunteer_detail'),
    path('<int:pk>/events/', EventListView.as_view(template_name='users/events.html'), name='events'),
    path('<int:pk>/certificates/', CertificateListView.as_view(template_name='users/certificates.html'), name='certificates'),
    path('<int:pk>/reviews/', ReviewListView.as_view(template_name='users/reviews.html'), name='reviews'),
    path('edit/', UserEdit.as_view(template_name='users/edit.html'), name='edit'),
]
