from django.template.context_processors import static
from django.template.defaulttags import url
from django.urls.conf import path

from jobs import views

from jobs.views import DeleteTask

from jobs.views import TaskListView, CreateTaskView, UpdateTaskView, TaskView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', TaskListView.as_view(), name="task-list"),
    path('create', CreateTaskView.as_view(), name="task-create"),
    path('update/<int:pk>', views.UpdateTaskView.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view(), name="task-delete"),
    path('task/<int:pk>', TaskView.as_view(), name="task-view"),

]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
