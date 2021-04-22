"""todorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import Http404
from django.template.context_processors import static
from django.urls import path
from django.urls.conf import include
from django.urls.exceptions import NoReverseMatch

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('user.urls')),
      path('api/', include('userprofile.urls')),
      path('job/', include('jobs.urls')),
      path('manager/', include('manager.urls')),
      path('django_user_interaction_log/', include('django_user_interaction_log.urls')),
]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
