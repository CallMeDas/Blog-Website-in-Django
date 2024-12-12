
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.test),
    path('', views.loginn),
    path('signin/', views.signin),
    path('home/', views.home),
]
