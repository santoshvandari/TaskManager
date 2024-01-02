from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from TaskManager.models import TaskInfo
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'index.html')

def AddTask(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        task_desc = request.POST.get('taskname').strip()
        user = request.user
        task_status=False
        if task_desc and user and task_status==False:
            tasksave=TaskInfo(user=user,task_desc=task_desc,task_status=task_status)
            tasksave.save()
            return redirect('/')
        else:
            return render(request,'addtask.html',{'error':'Invalid Data'})
    return render(request,'addtask.html')