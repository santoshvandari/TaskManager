from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    
    return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request,'signup.html',{'error':'Username already exists'})
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
            user.save()
            login(request,user)
            return redirect('/login')
    return render(request,'signup.html')

def log_out(request):
    logout(request)
    return redirect('/login')