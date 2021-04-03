from django.template.defaulttags import url
from django.urls.conf import path

from user.views import UserRegistrationView

from user.views import UserLoginView

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    ]
