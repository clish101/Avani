from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser): 
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    insurance = models.CharField(max_length=200)
    insuranceID = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    current_medication = models.TextField(null=True, blank=True)
    preexisting_medication = models.TextField(null=True, blank=True)
    next_of_kin = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    npi= models.CharField(max_length=200)
    education = models.TextField()
    qualifications = models.TextField()
    places_worked = models.TextField()
    consultation_fee = models.CharField(max_length=200)
    venue_of_operation = models.CharField(max_length=200)
    insurance=models.CharField(max_length=200)
    insurance2=models.CharField(max_length=200, blank=True, null=True)
    insurance3=models.CharField(max_length=200, blank=True, null=True)
    insurance4=models.CharField(max_length=200, blank=True, null=True)
    insurance5=models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Appointment_Request(models.Model):
    app_date = models.DateField(default=timezone.now)
    patient_app = models.ForeignKey(Patient,related_name='patient_app', on_delete=models.CASCADE)
    doctor_app = models.ForeignKey(Doctor,related_name='doctor_app', on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    cancelled_by_patient = models.BooleanField(default=False)
    second_opinion = models.BooleanField(default=False)
    sent_to_patient = models.BooleanField(default=False)

class Second_Opinion(models.Model):
    app_date_second = models.DateField(default=date.today)
    patient_app_second= models.ForeignKey(Patient,related_name='patient_second', on_delete=models.CASCADE)
    doctor_app_second = models.ForeignKey(Doctor,related_name='doctor_second', on_delete=models.CASCADE)
    seen_second = models.BooleanField(default=False)
    accepted_second = models.BooleanField(default=False)
    cancelled_second = models.BooleanField(default=False)
    cancelled_by_patient_second = models.BooleanField(default=False)
    sent_to_patient_second = models.BooleanField(default=False)

class Patient_Rating_Second(models.Model):
    appointment_second = models.ForeignKey(Second_Opinion, on_delete=models.CASCADE)
    rate_second = models.CharField(max_length=200)
    review_second = models.TextField()

class Patient_Rating(models.Model):
    appointment = models.ForeignKey(Appointment_Request, on_delete=models.CASCADE)
    rate = models.CharField(max_length=200)
    review = models.TextField()

class Feedback(models.Model):
    appointment_feedback = models.ForeignKey(Appointment_Request, on_delete=models.CASCADE)
    prescription = models.TextField()
    notes = models.TextField()
    
class Feedback_Second(models.Model):
    second_opinion_feedback =models.ForeignKey(Second_Opinion, on_delete=models.CASCADE)
    prescription_second = models.TextField()
    notes_second = models.TextField()