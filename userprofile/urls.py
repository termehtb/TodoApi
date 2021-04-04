from django.urls.conf import path

from userprofile.views import UserProfileView

from userprofile import views

from userprofile.views import ProfileUpdate

urlpatterns = [
    path('profile', UserProfileView.as_view()),
    path('profile/update', ProfileUpdate.as_view()),

]
