from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from TaskManager.models import TaskInfo
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    tasklist= TaskInfo.objects.filter(user=user)
    if tasklist is not None:
        return render(request,'index.html',{'tasklist':tasklist})
    else:
        return render(request,'index.html')

def AddTask(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        user = request.user
        task_desc = request.POST.get('taskname').strip()
        task_status=False
        if task_desc and user and task_status==False:
            tasksave=TaskInfo(user=user,task_desc=task_desc,task_status=task_status)
            tasksave.save()
            return redirect('/')
        else:
            return render(request,'addtask.html')
    return render(request,'addtask.html')

@login_required(login_url='/login')
def DeleteTask(request,id):
    try:
        task = TaskInfo.objects.get(user=request.user,id=id)
        if task:
            task.delete()
        return redirect('/')
    except:
        return redirect('/')

@login_required(login_url='/login')
def UpdateTask(request,id):
    try:
        task=TaskInfo.objects.get(user=request.user,id=id)
        if task:    
            if task.task_status == False:
                task.task_status = True
            else:
                task.task_status = False
            task.save()
        return redirect('/')
    except:
        return redirect('/')
    
@login_required(login_url='/login')
def EditTask(request,id):
    try:
        task=TaskInfo.objects.get(user=request.user,id=id)
        if task:
            if request.method == 'POST':
                task_desc = request.POST.get('taskname').strip()
                if task_desc:
                    task.task_desc = task_desc
                    task.task_status = False
                    task.save()
                    return redirect('/')
                else:
                    return render(request,'edittask.html',{'error':'Invalid Data'})
            taskdesc=task.task_desc
            return render(request,'edittask.html',{'task':taskdesc})
        else:
            return redirect('/')
    except:
        return redirect('/')