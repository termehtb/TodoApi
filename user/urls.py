from django.template.defaulttags import url
from django.urls.conf import path
from django.conf.urls import url

from user.views import UserRegistrationView

from user.views import UserLoginView

from user import views

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', views.UserLoginView.as_view()),
    ]
