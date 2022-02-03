from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Patient, Doctor, User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class DoctorSignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'DR.'}), max_length=200)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'number'}), max_length=200)
    address = forms.CharField(widget=forms.Textarea)
    speciality = forms.CharField(max_length=200)
    npi = forms.CharField(max_length=200)
    education = forms.CharField(widget=forms.Textarea)
    qualifications = forms.CharField(widget=forms.Textarea)
    places_worked = forms.CharField(widget=forms.Textarea)
    consultation_fee = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number'}), max_length=200)
    venue_of_operation = forms.CharField(max_length=200)
    insurance = forms.CharField(max_length=200)
    insurance2 = forms.CharField(max_length=200, required=False)
    insurance3 = forms.CharField(max_length=200, required=False)
    insurance4 = forms.CharField(max_length=200, required=False)
    insurance5 = forms.CharField(max_length=200, required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.email = self.cleaned_data.get('email')
        doctor.name = self.cleaned_data.get('name')
        doctor.date_of_birth = self.cleaned_data.get('date_of_birth')
        doctor.gender = self.cleaned_data.get('gender')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.address = self.cleaned_data.get('address')
        doctor.speciality = self.cleaned_data.get('speciality')
        doctor.npi = self.cleaned_data.get('npi')
        doctor.education = self.cleaned_data.get('education')
        doctor.qualifications = self.cleaned_data.get('qualifications')
        doctor.places_worked = self.cleaned_data.get('places_worked')
        doctor.consultation_fee = self.cleaned_data.get('consultation_fee')
        doctor.venue_of_operation = self.cleaned_data.get('venue_of_operation')
        doctor.insurance = self.cleaned_data.get('insurance')
        doctor.insurance2 = self.cleaned_data.get('insurance2')
        doctor.insurance3 = self.cleaned_data.get('insurance3')
        doctor.insurance4 = self.cleaned_data.get('insurance4')
        doctor.insurance5 = self.cleaned_data.get('insurance5')
        doctor.save()

        return user


class DoctorUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'DR.'}), max_length=200)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'number'}), max_length=200)
    address = forms.CharField(widget=forms.Textarea)
    speciality = forms.CharField(max_length=200)
    npi = forms.CharField(max_length=200)
    education = forms.CharField(widget=forms.Textarea)
    qualifications = forms.CharField(widget=forms.Textarea)
    places_worked = forms.CharField(widget=forms.Textarea)
    consultation_fee = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number'}), max_length=200)
    venue_of_operation = forms.CharField(max_length=200)
    insurance = forms.CharField(max_length=200)
    insurance2 = forms.CharField(max_length=200, required=False)
    insurance3 = forms.CharField(max_length=200, required=False)
    insurance4 = forms.CharField(max_length=200, required=False)
    insurance5 = forms.CharField(max_length=200, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'name', 'date_of_birth', 'gender', 'phone',
                  'address', 'speciality', 'npi', 'education', 'qualifications', 'places_worked', 'consultation_fee', 'venue_of_operation', 'insurance', 'insurance2', 'insurance3', 'insurance4', 'insurance5']


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    insurance = forms.CharField(max_length=200)
    insuranceID = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    email = forms.EmailField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number'}), max_length=200)
    current_medication = forms.CharField(widget=forms.Textarea)
    preexisting_medication = forms.CharField(widget=forms.Textarea)
    next_of_kin = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.first_name = self.cleaned_data.get('first_name')
        patient.last_name = self.cleaned_data.get('last_name')
        patient.insurance = self.cleaned_data.get('insurance')
        patient.insuranceID = self.cleaned_data.get('insuranceID')
        patient.address = self.cleaned_data.get('address')
        patient.email = self.cleaned_data.get('email')
        patient.date_of_birth = self.cleaned_data.get('date_of_birth')
        patient.gender = self.cleaned_data.get('gender')
        patient.phone = self.cleaned_data.get('phone')
        patient.current_medication = self.cleaned_data.get(
            'current_medication')
        patient.preexisting_medication = self.cleaned_data.get(
            'preexisting_medication')
        patient.next_of_kin = self.cleaned_data.get('next_of_kin')
        patient.save()
        return user


class PatientUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200)

    insurance = forms.CharField(max_length=200)
    insuranceID = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    email = forms.EmailField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number'}), max_length=200)
    current_medication = forms.CharField(widget=forms.Textarea)
    preexisting_medication = forms.CharField(widget=forms.Textarea)
    next_of_kin = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['first_name', 'insurance', 'phone', 'email', 'date_of_birth', 'insuranceID',
                  'address', 'gender', 'current_medication', 'preexisting_medication', 'next_of_kin']
