# Generated by Django 3.1 on 2020-08-21 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='scheduledInterviews',
        ),
    ]
