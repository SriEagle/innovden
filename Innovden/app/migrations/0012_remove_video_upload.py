# Generated by Django 3.2.16 on 2022-10-19 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='upload',
        ),
    ]