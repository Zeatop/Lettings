from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls'))
]
