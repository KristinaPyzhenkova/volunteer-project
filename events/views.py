from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, get_object_or_404, render, reverse

from .models import Event, Follow, Function, Favorites
from .forms import EventForm, EventFormCreate
from django.contrib.auth.decorators import login_required


@login_required
def EventDetail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    following = Follow.objects.filter(user=request.user, event=event).exists()
    favorites = Favorites.objects.filter(user=request.user, event=event).exists()
    functions = Function.objects.filter(event=event)
    user_count = event.following.count()
    users_following = Follow.objects.filter(event=event)
    context = {
        'event': event,
        'following': following,
        'functions': functions,
        'user_count': user_count,
        'favorites': favorites,
        'users_following': users_following
    }
    return render(request, 'events/event_detail.html', context)


class EventsList(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'

@login_required
def profile_unfollow(request, pk):
    follow = get_object_or_404(Event, pk=pk)
    Follow.objects.filter(user=request.user, event=follow).delete()
    return redirect('events:event_detail', pk=pk)

@login_required
def profile_follow(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, event=event)
    if form.is_valid():
        fun = form.save(commit=False)
        fun.user = request.user
        fun.event = event
        fun.save()
        return redirect('events:event_detail', pk=pk)
    return render(
        request, 'events/follow.html', {'form': form}
    )

@login_required
def follow_index(request):
    follows = Follow.objects.filter(user=request.user)
    context = {
        'follows': follows
    }
    return render(request, 'events/events_follow.html', context)

@login_required
def profile_unfavorite(request, pk):
    favorite = get_object_or_404(Event, pk=pk)
    Favorites.objects.filter(user=request.user, event=favorite).delete()
    return redirect('events:event_detail', pk=pk)

@login_required
def profile_favorite(request, pk):
    favorite = get_object_or_404(Event, pk=pk)
    Favorites.objects.get_or_create(user=request.user, event=favorite)
    return redirect('events:event_detail', pk=pk)

@login_required
def favorites_index(request):
    favorites = Favorites.objects.filter(user=request.user)
    context = {
        'favorites': favorites
    }
    return render(request, 'events/events_favorites.html', context)


@login_required
def event_create(request):
    form = EventFormCreate(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.contact_user = request.user
        event.save()
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': event.pk}
        ))
    return render(
        request, 'events/create_event.html', {'form': form}
    )


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.contact_user:
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': event.pk}
        ))
    form = EventFormCreate(
        request.POST or None,
        files=request.FILES or None,
        instance=event
    )
    if form.is_valid():
        form.save()
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': event.pk}
        ))
    return render(
        request, 'events/create_event.html', {'form': form}
    )