# Generated by Django 3.2.5 on 2021-08-16 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_rename_sent_to_pa_secondtient_second_second_opinion_sent_to_patient_second'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField()),
                ('notes', models.TextField()),
                ('appointment_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.appointment_request')),
                ('second_opinion_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.second_opinion')),
            ],
        ),
    ]
