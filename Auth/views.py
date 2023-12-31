from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'signup.html')

def log_out(request):
    logout(request)
    return redirect('/login')