from django.contrib import admin
from .models import Doctor, Feedback, Feedback_Second, Patient, Patient_Rating, Patient_Rating_Second, User, Appointment_Request, Second_Opinion

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment_Request)
admin.site.register(Second_Opinion)
admin.site.register(Patient_Rating_Second)
admin.site.register(Patient_Rating)
admin.site.register(Feedback)
admin.site.register(Feedback_Second)
