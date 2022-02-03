# Generated by Django 3.2.5 on 2021-08-14 21:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_patient_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('doctor_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_app', to='patient.doctor')),
                ('patient_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_app', to='patient.patient')),
            ],
        ),
    ]
