# Generated by Django 4.2.6 on 2023-10-11 17:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="birth_date",
            new_name="birthdate",
        ),
    ]
