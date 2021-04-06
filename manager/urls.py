from django.urls.conf import path

from manager.views import UserView, AllTaskListView, UserRegistrationView


urlpatterns = [

    path('users',UserView.as_view(), name="user-view"),
    path('tasks', AllTaskListView.as_view(), name="task-view"),
    path('adduser', UserRegistrationView.as_view(), name="create-user"),

]
