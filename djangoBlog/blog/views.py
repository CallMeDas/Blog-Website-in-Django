from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginn(request):
    return render(request, 'loginn.html')

