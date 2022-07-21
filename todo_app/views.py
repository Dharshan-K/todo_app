from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Tasks
# Create your views here.


def tasks_view(request):
	task_list = Tasks.objects.all()
	return render(request,'index.html',{"task_list":task_list})

def addTask(request):
	new_task = Tasks(Title= request.POST['title'],
					description= request.POST['description'],)
					# status= request.POST['submit'])
	new_task.save()
	return HttpResponseRedirect('/tasksview/')

def deleteTask(request, task_id):
	remove_task = Tasks.objects.get(id=task_id)
	remove_task.delete()
	return HttpResponseRedirect('/tasksview/')

	
