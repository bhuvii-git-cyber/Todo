from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task 

# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
def mark_as_done(request,pk):
    task=Task.objects.get(pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_as_undone(request,pk):
    task=Task.objects.get(pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')
def edit(request,pk):
    get_task=Task.objects.get(pk=pk)
    if request.method=='POST':
        get_task.task=request.POST['task']
        get_task.save()
        return redirect('home')
    else:
        context={
            'data':get_task,
        }
        return render(request,'edit.html',context)
def delete(request,pk):
   get_task=Task.objects.get(pk=pk)
   get_task.delete()
   return redirect('home')


    



    

