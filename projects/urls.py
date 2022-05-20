from django.urls import path

from projects.views import ProjectDetail, ProjectsList

app_name = 'projects'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects_list'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
]
