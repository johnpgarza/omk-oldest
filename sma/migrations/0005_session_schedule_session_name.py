# Generated by Django 3.0.3 on 2020-03-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0004_attendance_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_schedule',
            name='session_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
