from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if authenticate(username=username,password=password) is not None:
            login(request)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    
    return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'signup.html')

def log_out(request):
    logout(request)
    return redirect('/login')