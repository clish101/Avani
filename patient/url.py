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

from django.contrib import auth
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('patientsignup/', views.PatientSignUpView.as_view(), name='patientsignup'),
    path('doctorsignup/', views.DoctorSignUpView.as_view(), name='doctorsignup'),
    path('booking/<int:userID>/', views.booking, name='booking'),
    path('appfeedback/', views.appfeedback, name='appfeedback'),
    path('reviewratings/', views.patient_reviews, name='reviewratings'),
    path('ratings/<int:id>/', views.patient_reviews_complete, name='ratings'),
    path('reviewratingss/<int:id>/', views.patient_reviews_second, name='reviewratingss'),
    path('notifications/', views.notifications, name='notifications'),
    path('personaldetails/', views.personaldetails, name='personaldetails'),
    path('consultationrequest/', views.consultation, name='consultationrequest'),
    path('regularappointments/', views.regularappointments, name='regularappointments'),
    path('medicalconditions/', views.conditions, name='medicalconditions'),
    path('patientlogin/', views.PatientLoginView.as_view(), name='patientlogin'),
    path('patientlogout/', auth_views.LogoutView.as_view(template_name='patient/home.html'), name='patientlogout'),
    path('patienthome/', views.patienthome, name='patienthome'),    
    path('make_an_appointment/<int:userID>/', views.make_an_appointment, name='appmake'),    
    path('delete/<int:id>/', views.delete_app, name='deleteapp'),    
    path('delete_second/<int:id>/', views.delete_second, name='deleteseco'),    
    path('secondop/<int:id>/', views.secondop, name='secondop'),    
    path('uploadsent/', views.uploadsend, name='upsend'),    
    path('feedbackpatient/<int:id>/', views.feedbackpatient, name='feedbackpatient'),    
    path('feedbackpatientsecond/<int:id>/', views.feedbackpatient_second, name='feedbackpatientsecond'),    
    path('deletepatient/', views.deletepatient, name='deletepatient'),    
    
]
