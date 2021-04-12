from django.urls.conf import path

from manager.views import UserView, AllTaskListView, UserRegistrationView , AdminRegistrationView

from manager import views

urlpatterns = [

    path('users',UserView.as_view(), name="user-view"),
    path('tasks', AllTaskListView.as_view(), name="task-view"),
    path('adduser', UserRegistrationView.as_view(), name="create-user"),
    path('admindelete', views.RemoveUser.as_view(), name="admin-delete"),
    path('signup', AdminRegistrationView.as_view(), name="register-admin"),

]
