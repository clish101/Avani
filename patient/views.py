from typing import ContextManager
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.db.models import Q
from django.views.generic import CreateView
from .models import Feedback, Feedback_Second, Patient, Patient_Rating, Patient_Rating_Second, User, Appointment_Request, Doctor, Second_Opinion
from .forms import PatientSignUpForm, DoctorSignUpForm, PatientUpdateForm
from datetime import datetime, timedelta, time
from django.contrib import messages


def home(request):
    doctors = Doctor.objects.all()
    query = request.POST.get('s')
    query1 = request.POST.get('i')

    if query:
        doctors = Doctor.objects.filter(
            Q(speciality__icontains=query))
    elif query1:
        doctors = Doctor.objects.filter(
            Q(insurance__icontains=query1) | Q(insurance2__icontains=query1) | Q(insurance3__icontains=query1) | Q(insurance4__icontains=query1) | Q(insurance5__icontains=query1))

    context = {'doctors': doctors}
    return render(request, 'patient\home.html', context)


def contact(request):
    return render(request, 'patient\contact.html')


def patientsignup(request):
    return render(request, 'patient\patientsignup.html')


def personaldetails(request):
    return render(request, 'patient\personaldetails.html')


def patientlogin(request):
    return render(request, 'patient\patientlogin.html')


def patienthome(request):
    doctors = Doctor.objects.all()
    query = request.POST.get('s')
    query1 = request.POST.get('i')

    if query:
        doctors = Doctor.objects.filter(
            Q(speciality__icontains=query))
    elif query1:
        doctors = Doctor.objects.filter(
            Q(insurance__icontains=query1) | Q(insurance2__icontains=query1) | Q(insurance3__icontains=query1) | Q(insurance4__icontains=query1) | Q(insurance5__icontains=query1))

    context = {'doctors': doctors}
    return render(request, 'patient\patienthome.html', context)


def consultation(request):
    doctors = Doctor.objects.all()
    appointments = Appointment_Request.objects.all()
    query = request.POST.get('s')
    query1 = request.POST.get('i')

    if query:
        doctors = Doctor.objects.filter(
            Q(speciality__icontains=query))
        appointments = Appointment_Request.objects.filter(
            Q(doctor_app__speciality__icontains=query))
    elif query1:
        doctors = Doctor.objects.filter(
            Q(insurance__icontains=query1) | Q(insurance2__icontains=query1) | Q(insurance3__icontains=query1) | Q(insurance4__icontains=query1) | Q(insurance5__icontains=query1))
        appointments = Appointment_Request.objects.filter(
            Q(doctor_app__insurance__icontains=query1) | Q(doctor_app__insurance2__icontains=query1) | Q(doctor_app__insurance3__icontains=query1) | Q(doctor_app__insurance4__icontains=query1) | Q(doctor_app__insurance5__icontains=query1))

    context = {'appointments': appointments, 'doctors': doctors}
    return render(request, 'patient\consultationrequest.html', context)


def regularappointments(request):
    doctors = Doctor.objects.all()
    query = request.POST.get('s')
    query1 = request.POST.get('i')

    if query:
        doctors = Doctor.objects.filter(
            Q(speciality__icontains=query))
    elif query1:
        doctors = Doctor.objects.filter(
            Q(insurance__icontains=query1) | Q(insurance2__icontains=query1) | Q(insurance3__icontains=query1) | Q(insurance4__icontains=query1) | Q(insurance5__icontains=query1))

    context = {'doctors': doctors}
    return render(request, 'patient/regularappointments.html', context)


@login_required(login_url='/patientlogin/')
def booking(request, userID):
    try:
        doctor = Doctor.objects.filter(user__id=userID)
        context = {'doctor': doctor}
        return render(request, 'patient/booking.html', context)
    except:
        messages.warning(
                request, "You have to be logged in as a patient to book an appointment")
        return redirect('booking')


def notifications(request):
    upcoming_appointments = Appointment_Request.objects.all()
    upcoming_appointments_second = Second_Opinion.objects.filter(
        Q(accepted_second=True) & Q(seen_second=False))
    pending_appointments = Second_Opinion.objects.filter(
        Q(accepted_second=False) & Q(seen_second=False))
    cancelled_appointments = Second_Opinion.objects.filter(
        Q(cancelled_second=True) & Q(seen_second=False))
    context = {'upcoming_appointments': upcoming_appointments, 'pending_appointments': pending_appointments,
               'cancelled_appointments': cancelled_appointments, 'upcoming_appointments_second': upcoming_appointments_second}
    return render(request, 'patient/notifications.html', context)


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    success_url = '/patienthome'
    template_name = 'patient\patientsignup.html'


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'doctor\doctorsignup.html'
    success_url = '/doctor/doctorhome'


class PatientLoginView(LoginView):
    template_name = 'patient/patientlogin.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return '/patienthome'


def conditions(request):
    try:
        if request.method == 'POST':
            u_form = PatientUpdateForm(request.POST, instance=request.user.patient)

            if u_form.is_valid():
                u_form.save()

                return redirect('patienthome')
        else:
            u_form = PatientUpdateForm(instance=request.user.patient)

        context = {'u_form': u_form}
        return render(request, 'patient/medicalconditions.html', context)

    except:
        messages.warning(
                request, "You have to be a patient to access patient's profile")
        return redirect('home')
   

def make_an_appointment(request, userID):
    try:
        what = request.GET.get('app_date')
        patient_app = request.user.patient
        doctor_user = User.objects.get(id=userID)
        doctor_app = doctor_user.doctor
        created = Appointment_Request.objects.get_or_create(
            app_date=what, patient_app=patient_app, doctor_app=doctor_app)
        if created:
            return redirect('notifications')
        else:
            return HttpResponse('Appointment with the doctor was already sent')
    except:
        messages.warning(
                request, "You have to be logged in as a patient to book")
        return redirect('regularappointments')


def delete_app(request, id):
    app = Appointment_Request.objects.filter(id=id)
    app.delete()
    return redirect('notifications')


def delete_second(request, id):
    app = Second_Opinion.objects.filter(id=id)
    app.delete()
    return redirect('notifications')


def secondop(request, id):
    try:
        what = request.GET.get('app_date')
        app = Appointment_Request.objects.get(id=id)
        app.second_opinion = True
        app.save()
        Second_Opinion.objects.get_or_create(
            app_date_second=what, patient_app_second=app.patient_app, doctor_app_second=app.doctor_app)

        return redirect('consultationrequest')

    except:
        messages.warning(
                request, "Please provide a date for your Second request consultation")
        return redirect('consultationrequest')

def uploadsend(request):
    if request.method =='POST':
        # for item in request.POST.getlist('checking'):
        #     print(item)
           
        # print(request.POST)
        if 'upload' in request.POST:
            dates = request.POST.getlist('dating')
            doctors = request.POST.getlist('checking')
            
            for doctor in doctors:
                daktari = Doctor.objects.get(name=doctor)
                date = doctors.index(doctor)
                Second_Opinion.objects.get_or_create(
            app_date_second=dates[date] or datetime.today().date(), patient_app_second=request.user.patient, doctor_app_second=daktari)
                
            return redirect('regularappointments')


    
    



def patient_reviews(request):
    complete_second = Second_Opinion.objects.filter(seen_second=True)
    complete_appointments = Appointment_Request.objects.filter(seen=True)

    context = {'complete_second': complete_second,
               'complete_appointments': complete_appointments}
    return render(request, 'patient/reviewsratings.html', context)


def patient_reviews_second(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rated')
        review = request.POST.get('reviewed')
        rated_second = Second_Opinion.objects.get(id=id)
        Patient_Rating_Second.objects.get_or_create(
            appointment_second=rated_second, rate_second=rating, review_second=review)

    return redirect('home')


def patient_reviews_complete(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rated')
        review = request.POST.get('reviewed')
        rated_second = Appointment_Request.objects.get(id=id)
        Patient_Rating.objects.get_or_create(
            appointment=rated_second, rate=rating, review=review)

    return redirect('home')

def feedbackpatient(request, id):
    feedback = Appointment_Request.objects.get(pk=id)
    if request.method=='POST':
        prescription=request.POST.get('prescription')
        notes=request.POST.get('notes')
    
        Feedback.objects.get_or_create(appointment_feedback=feedback, prescription=prescription, notes=notes)
    return redirect('feedback')

def feedbackpatient_second(request, id):
    feedback = Second_Opinion.objects.get(pk=id)
    if request.method=='POST':
        prescription=request.POST.get('prescription')
        notes=request.POST.get('notes')
    
        Feedback_Second.objects.get_or_create(second_opinion_feedback=feedback, prescription_second=prescription, notes_second=notes)
    return redirect('feedback')

def appfeedback(request):
    feedbacks= Feedback.objects.all()
    feedbackss = Feedback_Second.objects.all()
    context = {"feedbacks":feedbacks, "feedbackss":feedbackss}
    return render(request, 'patient/appfeedback.html',context)

def deletepatient(request):
    patient = Patient.objects.filter(user= request.user.patient)
    patient.delete()
    return redirect('home')