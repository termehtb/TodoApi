from django.urls.conf import path

from jobs import views

from jobs.views import DeleteTask

from jobs.views import TaskListView, CreateTaskView, UptadeTaskView, AllTaskListView

urlpatterns = [
    path('list/', TaskListView.as_view(), name="task-list"),
    path('create', CreateTaskView.as_view(), name="task-create"),
    path('update/<int:pk>', UptadeTaskView.as_view(), name="task-update"),
    path('delete/<int:pk>', DeleteTask.as_view(), name="task-delete"),
    path('users/', views.userlist, name="user-view"),
    path('tasks/', AllTaskListView.as_view(), name="task-view"),


]

