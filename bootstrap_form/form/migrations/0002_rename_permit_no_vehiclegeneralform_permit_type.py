# Generated by Django 3.2.3 on 2021-06-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclegeneralform',
            old_name='permit_no',
            new_name='permit_type',
        ),
    ]
