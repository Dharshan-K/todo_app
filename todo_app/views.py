from django.shortcuts import render
from .models import Tasks
# Create your views here.


def tasks_view(request):
	task_list = Tasks.objects.all()
	return render(request,'index.html',{"task_list":task_list})

	
