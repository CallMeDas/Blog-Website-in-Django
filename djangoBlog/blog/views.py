from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test (request):
    return HttpResponse('welcome')

def loginn(request):
    return render(request, 'loginn.html')

def signin(request):
    return render(request, 'signin.html')
    

