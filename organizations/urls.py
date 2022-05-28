from django.urls import path

from .views import OrganizationDetail, OrganizationsList
from . import views

app_name = 'organizations'

urlpatterns = [
    path('', OrganizationsList.as_view(), name='organizations_list'),
    path('<int:pk>/', OrganizationDetail.as_view(), name='organization_detail'),
    path('organization_create/', views.organization_create, name='organization_create'),
]