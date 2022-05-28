from django.urls import path

from projects.views import ProjectDetail, ProjectsList
from . import views

app_name = 'projects'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects_list'),
    path('<int:pk>/', views.ProjectDetail, name='project_detail'),
    path('<int:pk>/unfavorite', views.profile_unfavorite, name='profile_unfavorite'),
    path('<int:pk>/favorite', views.profile_favorite, name='profile_favorite'),
    path('<int:pk>/favorite_part', views.profile_favorite_part, name='profile_favorite_part'),

]
