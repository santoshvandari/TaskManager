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
        task_desc = request.POST.get('taskname')
        user = request.user
        status=False
        TaskInfo.objects.create(user=user,task_desc=task_desc)
        return redirect('/addtask')