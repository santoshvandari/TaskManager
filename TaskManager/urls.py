"""
URL configuration for Task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from TaskManager import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addtask/',views.AddTask,name='addtask'),
    path('deletetask/<id>/',views.DeleteTask,name='deletetask'),
    path('update/<id>/',views.UpdateTask,name='update'),
    path('edit/<id>/',views.EditTask,name='edit'),
    path('profile/',views.Profile,name='profile'),
]
