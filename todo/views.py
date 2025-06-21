from django.http import HttpResponse
from django.shortcuts import render
from .models import Task 

# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return HttpResponse ("the form is submitted")
