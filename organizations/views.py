from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, get_object_or_404, render, reverse

from .models import Organization
from .forms import OrganizationForm

class OrganizationDetail(DetailView):
    model = Organization
    template_name = 'organizations/organization_detail.html'
    context_object_name = 'organization'


class OrganizationsList(ListView):
    model = Organization
    template_name = 'organizations/organizations.html'
    context_object_name = 'organizations'


def organization_create(request):
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        organization = form.save(commit=False)
        organization.leader = request.user
        organization.save()
        return redirect(reverse(
            'organizations:organization_detail', kwargs={'pk': organization.pk}
        ))
    return render(
        request, 'organizations/create_organization.html', {'form': form}
    )