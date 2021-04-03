from django.urls.conf import path

from jobs import views

urlpatterns = [
    path('list/', views.taskList, name="task-list"),
    path('detail/<int:pk>/', views.taskDetail, name="task-detail"),
    path('create', views.taskCreate, name="task-create"),
    path('update/<int:pk>/', views.taskUpdate, name="task-update"),
    path('delete/<int:pk>/', views.taskDelete, name="task-delete"),

]

