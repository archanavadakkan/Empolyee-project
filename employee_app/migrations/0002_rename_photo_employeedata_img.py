# Generated by Django 3.2.18 on 2023-03-21 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedata',
            old_name='photo',
            new_name='img',
        ),
    ]
