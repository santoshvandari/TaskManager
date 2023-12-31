from django.shortcuts import render,redirect

# Create your views here.
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'signup.html')