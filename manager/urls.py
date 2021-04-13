from django.urls.conf import path

from manager.views import UserView, AllTaskListView, UserRegistrationView , AdminRegistrationView

from manager import views

from manager.views import RemoveUser

urlpatterns = [

    path('users',UserView.as_view(), name="user-view"),
    path('tasks', AllTaskListView.as_view(), name="task-view"),
    path('adduser', UserRegistrationView.as_view(), name="create-user"),
    path('remove/<slug:pk>', RemoveUser.as_view(), name="remove-user"),
    path('signup', AdminRegistrationView.as_view(), name="register-admin"),

]
