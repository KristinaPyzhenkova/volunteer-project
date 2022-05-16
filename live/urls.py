from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from live.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizations/', include('organizations.urls', namespace='organizations')),
    path('events/', include('events.urls', namespace='events')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('', HomeView.as_view(template_name='index.html'), name='index'),
    path('auth/', include('auth_users.urls', namespace='auth_users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('volunteers/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
