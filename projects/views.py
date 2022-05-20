from django.views.generic import DetailView, ListView

from .models import Project

class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'


class ProjectsList(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
