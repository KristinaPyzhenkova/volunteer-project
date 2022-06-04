from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, get_object_or_404, render, reverse
from datetime import datetime

from .models import Event, Follow, Function, Favorites
from .filters import Event_Filter
from .forms import EventForm, EventFormCreate, FunctionFormCreate
from django.contrib.auth.decorators import login_required


@login_required
def EventDetail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    following = Follow.objects.filter(user=request.user, event=event).exists()
    favorites = Favorites.objects.filter(user=request.user, event=event).exists()
    following_func = []
    for i in Follow.objects.filter(user=request.user, event=event):
        following_func.append(i.function.pk)
    functions = Function.objects.filter(event=event)
    len_functions = len(functions)
    user_count = event.following.count()
    users_following = Follow.objects.filter(event=event)
    count_u=[]
    for i in functions:
        count_u.append(int(i.count))
    count_remainder = (True if (sum(count_u)>user_count) else False)
    count_u_func={}
    for i in functions:
        count_u_func[i.pk] = i.following.count()
    context = {
        'event': event,
        'following': following,
        'functions': functions,
        'user_count': user_count,
        'favorites': favorites,
        'users_following': users_following,
        'len_functions': len_functions,
        'count_remainder': count_remainder,
        'following_func': following_func,
        'count_u_func': count_u_func
    }
    return render(request, 'events/event_detail.html', context)


def EventsList(request):
    events = Event.objects.all()
    filter = Event_Filter(request.GET, queryset=events)
    events = filter.qs
    context = {'events': events, 'filter': filter}
    return render(request, 'events/events.html', context)


class EventsListActive(ListView):
    model = Event
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events_all=Event.objects.all()
        events_pk=[]
        for event_one in events_all:
            functions=Function.objects.filter(event=event_one)
            count_u = []
            for i in functions:
                count_u.append(int(i.count))
            if sum(count_u)>event_one.following.count() and event_one.date_end.date()>datetime.now().date():
                events_pk.append(event_one.pk)
        events=events_all.filter(pk__in=events_pk)
        filter = Event_Filter(self.request.GET, queryset=events)
        events = filter.qs
        context['events'] = events
        context['filter'] = filter
        return context


class EventsListProcess(ListView):
    model = Event
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events_all=Event.objects.all()
        events_pk=[]
        for event_one in events_all:
            functions=Function.objects.filter(event=event_one)
            count_u = []
            for i in functions:
                count_u.append(int(i.count))
            if sum(count_u)==event_one.following.count() and event_one.date_end.date()>datetime.now().date():
                events_pk.append(event_one.pk)
        events=events_all.filter(pk__in=events_pk)
        filter = Event_Filter(self.request.GET, queryset=events)
        events = filter.qs
        context['events'] = events
        context['filter'] = filter
        return context


class EventsListClose(ListView):
    model = Event
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events_all=Event.objects.all()
        events_pk=[]
        for event_one in events_all:
            if event_one.date_end.date()<datetime.now().date():
                events_pk.append(event_one.pk)
        events=events_all.filter(pk__in=events_pk)
        filter = Event_Filter(self.request.GET, queryset=events)
        events = filter.qs
        context['events'] = events
        context['filter'] = filter
        return context


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
        'follows': follows,
        'condition': True
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
def profile_unfollow_func(request, pk_event, pk_funk):
    event_follow = get_object_or_404(Event, pk=pk_event)
    func_follow = get_object_or_404(Function, event_id=event_follow.pk, pk=pk_funk)
    Follow.objects.filter(user=request.user, event=event_follow, function=func_follow).delete()
    return redirect('events:event_detail', pk=event_follow.pk)

@login_required
def profile_follow_func(request, pk_event, pk_funk):
    event_follow = get_object_or_404(Event, pk=pk_event)
    func_follow = get_object_or_404(Function, event_id=event_follow.pk,pk=pk_funk)
    Follow.objects.get_or_create(user=request.user, event=event_follow, function=func_follow)
    return redirect('events:event_detail', pk=event_follow.pk)



@login_required
def favorites_index(request):
    favorites = Favorites.objects.filter(user=request.user)
    context = {
        'follows': favorites,
        'condition': True
    }
    return render(request, 'events/events_follow.html', context)

@login_required
def own_index(request):
    owns = Event.objects.filter(contact_user=request.user)
    context = {
        'owns': owns,
        'condition': False
    }
    return render(request, 'events/events_follow.html', context)

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
def function_create(request, pk):
    form = FunctionFormCreate(request.POST or None)
    event = Event.objects.get(pk=pk)
    if form.is_valid():
        function = form.save(commit=False)
        function.event = event
        function.save()
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': event.pk}
        ))
    return render(
        request, 'events/create_function.html', {'form': form}
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

@login_required
def function_edit(request, pk):
    function = get_object_or_404(Function, pk=pk)
    if request.user != function.event.contact_user:
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': function.event.pk}
        ))
    form = FunctionFormCreate(
        request.POST or None,
        files=request.FILES or None,
        instance=function
    )
    if form.is_valid():
        form.save()
        return redirect(reverse(
            'events:event_detail', kwargs={'pk': function.event.pk}
        ))
    return render(
        request, 'events/create_event.html', {'form': form}
    )
    # FunFormSet=inlineformset_factory(Event, Function, fields=('name','description','task','condition','count'),extra=1)
    # function = get_object_or_404(Function, pk=pk)
    # formset = FunFormSet(
    #     # request.POST,
    #     # files=request.FILES,
    #     initial=function.event
    # )
    # # if request.method == 'POST':
    # #     formset=FunFormSet(request.POST,initial=function.event)
    # if formset.is_valid():
    #     formset.save()
    #     return redirect('events:event_detail', pk=function.event.pk)
    # return render(
    #     request, 'events/create_function.html', {'form': formset}
    # )