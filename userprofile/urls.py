from django.urls.conf import path

from userprofile.views import UserProfileView

urlpatterns = [
    path('profile', UserProfileView.as_view()),
    ]
