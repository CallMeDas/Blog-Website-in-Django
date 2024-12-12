from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout

# Create your views here.

def test (request):
    return HttpResponse('welcome')

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username= username, password= password)
        if userr is not None:
            login(request, userr)
            return redirect ('/home')
        else:
            return redirect('/loginn')
    
        
    return render(request, 'loginn.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        print(auth_user.username)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'signin.html')

def home(request):
    context = {
        "posts" : posts.objects.all()
    }
    return render(request, 'home.html', context)
    

