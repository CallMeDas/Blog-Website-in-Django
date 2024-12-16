from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts
from . import models
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
            return render(request, 'loginn.html',{'error': 'Incorrect Username or Password.'})
    
        
    return render(request, 'loginn.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        if User.objects.filter(username=name).exists():
            return render(request, 'signin.html', {'error': 'Username already exists!'})
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'signin.html')

def home(request):
    context = {
        "posts" : posts.objects.all()
    }
    return render(request, 'home.html', context)
    


def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.posts(title=title, content= content, author=request.user)
        npost.save()
        return redirect('/home')
    return render (request, 'newpost.html')

def myPost(request):
    context = {'post': posts.objects.filter(author=request.user)}
    return render(request, 'mypost.html', context)


def signOut(request):
    
    logout(request)
    return redirect ('/home')