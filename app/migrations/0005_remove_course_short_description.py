# Generated by Django 3.2.16 on 2022-10-17 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_course_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='short_description',
        ),
    ]
