from django.template.defaulttags import url
from django.urls.conf import path
from django.conf.urls import url

from user.views import UserRegistrationView

from user.views import UserLoginView

from user import views


urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    url(r'^signin', views.UserLoginView.as_view()),
    path('delete', views.DeleteUser.as_view()),
    url('deactive', views.Deactive.as_view()),

]
handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'

