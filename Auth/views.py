from django.shortcuts import render

# Create your views here.
def log_in(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'Auth/signup.html')