# Generated by Django 3.2.16 on 2022-10-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_course_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]