# Generated by Django 3.2.3 on 2021-06-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('status_change_date', models.DateField(blank=True, null=True)),
                ('vehicle_onwer', models.CharField(blank=True, max_length=50, null=True)),
                ('onwer_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('onwer_address', models.CharField(blank=True, max_length=50, null=True)),
                ('onn_vehicle', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatutoryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_tax', models.CharField(blank=True, max_length=20, null=True)),
                ('road_tax_expiry', models.DateField(blank=True, null=True)),
                ('fitness', models.CharField(blank=True, max_length=20, null=True)),
                ('fitness_expiry', models.DateField(blank=True, null=True)),
                ('insurance', models.CharField(blank=True, max_length=20, null=True)),
                ('insurance_expiry', models.DateField(blank=True, null=True)),
                ('pollution', models.CharField(blank=True, max_length=20, null=True)),
                ('pollution_expiry', models.DateField(blank=True, null=True)),
                ('permit', models.CharField(blank=True, max_length=20, null=True)),
                ('permit_expiry', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleGeneralForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('vehicle_no', models.CharField(blank=True, max_length=20, null=True)),
                ('wheeler', models.CharField(blank=True, max_length=20, null=True)),
                ('rfid_tag', models.CharField(blank=True, max_length=20, null=True)),
                ('transporter', models.CharField(blank=True, max_length=20, null=True)),
                ('rc_no', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle_temp_no', models.CharField(blank=True, max_length=20, null=True)),
                ('chasis_no', models.CharField(blank=True, max_length=20, null=True)),
                ('permit_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
