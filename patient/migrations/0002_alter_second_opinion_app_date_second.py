# Generated by Django 3.2.5 on 2021-08-19 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='second_opinion',
            name='app_date_second',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
