# Generated by Django 3.2.5 on 2021-08-14 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20210814_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default=False, max_length=200),
            preserve_default=False,
        ),
    ]
