from django.contrib import messages
import patient
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from patient.models import Appointment_Request, Doctor, Feedback, Feedback_Second, Patient_Rating, Patient_Rating_Second, Second_Opinion
from patient.forms import DoctorUpdateForm
from django.db.models import Q
from django.http import FileResponse, request
import io

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def download(request, id):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    opinion = Second_Opinion.objects.get(pk=id)
    patient_name = opinion.patient_app_second.first_name
    patient_insurance = opinion.patient_app_second.insurance
    patient_phone = opinion.patient_app_second.phone
    patient_email = opinion.patient_app_second.email
    patient_date_of_birth = opinion.patient_app_second.date_of_birth
    patient_insuranceId = opinion.patient_app_second.insuranceID
    patient_address = opinion.patient_app_second.address
    patient_gender = opinion.patient_app_second.gender
    patient_current_medication = opinion.patient_app_second.current_medication
    patient_preexisting_medication = opinion.patient_app_second.preexisting_medication
    patient_next_of_kin = opinion.patient_app_second.next_of_kin

    # context = {'appointments':appointments, 'opinions':opinions}
    # return render(request,'doctor/appointments.html', context)
    print(patient_name)
    lines = [
        "Patient's Name: " + patient_name,
        "",
        "",
        "Insurance: " + patient_insurance,
        "",
        "",
        "Contacts: " + patient_phone,
        "",
        "",
        "Email: " + patient_email,
        "",
        "",
        "Date of Birth: " + str(patient_date_of_birth),
        "",
        "",
        "Member ID: " + patient_insuranceId,
        "",
        "",
        "Address: " + patient_address,
        "",
        "",
        "Gender: " + patient_gender,
        "",
        "",
        "Current Medication: " + patient_current_medication,
        "",
        "",
        "Preexisting Medication: " + patient_preexisting_medication,
        "",
        "",
        "Next of Kin: " + patient_next_of_kin,
        "",
        "",
        "Please Give me an A+",
        "Thank you in Advance"
    ]
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='patientmedicalinformation.pdf')


def doctorsignup(request):
    return render(request, 'doctor\doctorsignup.html')


def doctordetails(request):
    return render(request, 'doctor\doctordetails.html')


def approvals(request):
    return render(request, 'doctor\pendingapprovals.html')


def appointments(request):
    opinions = Second_Opinion.objects.all()
    appointments = Appointment_Request.objects.filter(
        doctor_app=request.user.doctor)
    context = {'appointments': appointments, 'opinions': opinions}
    return render(request, 'doctor/appointments.html', context)


def ratings(request):
    regular_ratings = Patient_Rating.objects.filter(
        appointment__doctor_app=request.user.doctor)
    second_ratings = Patient_Rating_Second.objects.filter(
        appointment_second__doctor_app_second=request.user.doctor)
    context = {'regular_ratings': regular_ratings,
               "second_ratings": second_ratings}
    return render(request, 'doctor/ratings.html', context)


def profile(request):
    try:
        if request.method == 'POST':
            u_form = DoctorUpdateForm(request.POST, instance=request.user.doctor)

            if u_form.is_valid():
                u_form.save()

                return redirect('doctorhome')
        else:
            u_form = DoctorUpdateForm(instance=request.user.doctor)

        context = {'u_form': u_form}

        return render(request, 'doctor/profile.html', context)
    except:
        messages.warning(
                request, "You have to be a doctor to access doctor's profile")
        return redirect('doctorhome')
   

class DoctorLoginView(LoginView):
    template_name = 'doctor/doctorlogin.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return '/doctor/doctorhome'


def doctorhome(request):
    return render(request, 'doctor\doctorhome.html')


def seen(request, id):
    appointment = Appointment_Request.objects.get(pk=id)
    appointment.seen = True
    appointment.save()
    return redirect('appointments')


def seensecond(request, id):
    appointment = Second_Opinion.objects.get(pk=id)
    appointment.seen_second = True
    appointment.save()
    return redirect('appointments')


def accepted(request, id):
    appointment = Second_Opinion.objects.get(id=id)
    appointment.accepted_second = True
    appointment.save()
    return redirect('appointments')


def cancelled(request, id):
    appointment = Second_Opinion.objects.get(id=id)
    appointment.cancelled_second = True
    appointment.save()
    return redirect('appointments')


def seenappointments(request):
    appointments = Appointment_Request.objects.filter(seen=True)
    opinions = Second_Opinion.objects.filter(seen_second=True)
    context = {"appointments": appointments, "opinions": opinions}
    return render(request, 'doctor/feedback.html', context)


def allratedappointments(request):

    complete_regulars = Patient_Rating.objects.all()
    complete_seconds = Patient_Rating_Second.objects.all()
    query = request.POST.get('s')
    query1 = request.POST.get('i')

    if query:
        complete_regulars = Patient_Rating.objects.filter(
            Q(appointment__doctor_app__speciality__icontains=query))
    elif query1:
        complete_seconds = Patient_Rating_Second.objects.filter(
            Q(appointment_second__doctor_app_second__insurance__icontains=query1) | Q(appointment_second__doctor_app_second__insurance2__icontains=query1) | Q(appointment_second__doctor_app_second__insurance3__icontains=query1) | Q(appointment_second__doctor_app_second__insurance4__icontains=query1) | Q(appointment_second__doctor_app_second__insurance5__icontains=query1))
    elif query:
        complete_regulars = Patient_Rating_Second.objects.filter(
            Q(appointment_second__doctor_app_second__speciality__icontains=query))
    elif query1:
        complete_seconds = Patient_Rating.objects.filter(
            Q(appointment__doctor_app__insurance__icontains=query1) | Q(appointment__doctor_app__insurance2__icontains=query1) | Q(appointment__doctor_app__insurance3__icontains=query1) | Q(appointment__doctor_app__insurance4__icontains=query1) | Q(appointment__doctor_app__insurance5__icontains=query1))

    
    context = {"complete_regulars": complete_regulars,
               "complete_seconds": complete_seconds}
    return render(request, 'doctor/completes.html', context)

def deletedoctor(request):
    doctor = Doctor.objects.get(user=request.user.doctor)
    doctor.delete()
    return redirect('home')
