from django.urls import path
from . import views
urlpatterns=[
	path('tasksview/', views.tasks_view, name="taskview"),
	path('addtask', views.addTask),
	path('deletetask/<int:task_id>',views.deleteTask)
	]