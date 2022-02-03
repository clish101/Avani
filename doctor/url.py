"""AVANIPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    

    path('doctordetails/', views.doctordetails, name='doctordetails'),
    path('appointments/', views.appointments, name='appointments'),
    path('profile/', views.profile, name='profile'),
    path('feedback/', views.seenappointments, name='feedback'),
    path('ratings/', views.ratings, name='ratings'),
    path('doctorlogin/', views.DoctorLoginView.as_view(), name='doctorlogin'),
    path('pendingapprovals/', views.approvals, name='pendingapprovals'),
    path('doctorlogout/',LogoutView.as_view(template_name='patient/home.html'), name='doctorlogout'),
    path('doctorhome/', views.doctorhome, name='doctorhome'),
    path('seen/<int:id>/', views.seen, name='seen'),
    path('seensecond/<int:id>/', views.seensecond, name='seensecond'),
    path('download/<int:id>/', views.download, name='download'),
    path('accepted/<int:id>/', views.accepted, name='accepted'),
    path('cancelled/<int:id>/', views.cancelled, name='cancelled'),
    path('allratedappointments/', views.allratedappointments, name='allratedappointments'),
    path('deletedoctor/', views.deletedoctor, name='deletedoctor'),
   
]
