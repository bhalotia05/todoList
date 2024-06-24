from django.shortcuts import render, HttpResponse, redirect
from home.models import Task
# Create your views here.
def home(request):
    context={'success' : False }
    if(request.method=="POST"):
        #handle the form
        title=request.POST['title']
        desc=request.POST['desc']
        # print(title,desc)
        ins=Task(TaskTitle=title, TaskDesc=desc)
        ins.save()
        context={'success' : True }

    return render(request,'index.html', context)

def tasks(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.TaskTitle = request.POST['title']
        task.TaskDesc = request.POST['desc']
        task.save()
        return redirect('tasks')
    return render(request, 'update_task.html', {'task': task})

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('tasks')