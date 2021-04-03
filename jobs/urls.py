from django.urls.conf import path

from jobs import views

urlpatterns = [
    path('list/', views.taskList, name="task-list"),
    path('detail/<int:id>', views.taskDetail, name="task-detail"),
    path('create', views.taskCreate, name="task-create"),
    path('update/<int:id>', views.taskUpdate, name="task-update"),
    path('delete/<int:id>', views.taskDelete, name="task-delete"),

]

