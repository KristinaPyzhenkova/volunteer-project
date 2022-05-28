from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Project
from events.models import Favorites, Event
from django.contrib.auth.decorators import login_required

@login_required
def ProjectDetail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    events_project = project.events.all()
    favorites = [Favorites.objects.filter(user=request.user, event=event).exists() for event in events_project]
    if favorites.count(True)==len(favorites):
        favorites = True
    elif True in favorites and False in favorites:
        favorites = 'part'
    else:
        favorites = False
    context = {
        'project': project,
        'events_project': events_project,
        'favorites': favorites
    }
    return render(request, 'projects/project_detail.html', context)


class ProjectsList(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'


@login_required
def profile_unfavorite(request, pk):
    project = get_object_or_404(Project, pk=pk)
    events_project = project.events.all()
    for event in events_project:
        favorite = get_object_or_404(Event, pk=event.pk)
        Favorites.objects.filter(user=request.user, event=favorite).delete()
    return redirect('projects:project_detail', pk=pk)


@login_required
def profile_favorite(request, pk):
    project = get_object_or_404(Project, pk=pk)
    events_project = project.events.all()
    for event in events_project:
        favorite = get_object_or_404(Event, pk=event.pk)
        Favorites.objects.get_or_create(user=request.user, event=favorite)
    return redirect('projects:project_detail', pk=pk)


@login_required
def profile_favorite_part(request, pk):
    project = get_object_or_404(Project, pk=pk)
    events_project = project.events.all()
    # event = [event for event in events_project]
    # favorites = [Favorites.objects.filter(user=request.user, event=event).exists() for event in events_project]
    # for index in range(len(favorites)):
    #     if favorites[index] == True:
    #         favorite = event[index]
    #         Favorites.objects.filter(user=request.user, event=favorite).delete()
    for event in events_project:
        favorite = get_object_or_404(Event, pk=event.pk)
        Favorites.objects.get_or_create(user=request.user, event=favorite)
    return redirect('projects:project_detail', pk=pk)

