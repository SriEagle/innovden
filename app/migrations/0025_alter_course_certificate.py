# Generated by Django 3.2.16 on 2022-10-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
    ]
