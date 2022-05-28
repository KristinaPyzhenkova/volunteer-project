from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Avg
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from events.models import UserEvent, Event
from users.forms import UserEditForm
from users.models import User, ReviewUser, Certificate


class UserDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        rating = ReviewUser.objects.filter(volunteer=self.object)
        events = UserEvent.objects.filter(user=self.object)
        context['rating'] = rating.aggregate(Avg('rating'))['rating__avg']
        context['stats_review'] = rating.count()
        context['stats_event'] = events.count()

        return context


class UserListView(ListView):
    model = User


class EventListView(ListView):
    def get_queryset(self):
        events = Event.objects.filter(userevent__user=self.kwargs['pk'])
        return events


class ReviewListView(ListView):
    def get_queryset(self):
        reviews = ReviewUser.objects.filter(volunteer=self.kwargs['pk'])
        return reviews


class CertificateListView(ListView):
    def get_queryset(self):
        certificates = Certificate.objects.filter(user=self.kwargs['pk'])
        return certificates


class UserEdit(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('users:volunteer_detail', kwargs={'pk': self.request.user.pk})
