# Generated by Django 4.2.7 on 2023-11-06 14:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfoliov2", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personalinfo",
            old_name="headder_description",
            new_name="header_description",
        ),
    ]