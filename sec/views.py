from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks=Task.objects.all().order_by('-updated_at')
    
    context={
        'data':tasks,
    }    
   
    return render(request,'home.html',context)
    