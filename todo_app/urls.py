from django.urls import path
from . import views
urlpatterns=[
	path('tasklist', views.tasks_view, name="taskview"),
	]