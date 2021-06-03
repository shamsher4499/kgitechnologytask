from django.db import models

# Create your models here.



class VehicleGeneralForm(models.Model):
    is_active = models.BooleanField(default=True, null=True, blank=True)
    vehicle_no = models.CharField(max_length=20, null=True, blank=True)
    wheeler = models.CharField(max_length=20, null=True, blank=True)
    rfid_tag = models.CharField(max_length=20, null=True, blank=True)
    transporter = models.CharField(max_length=20, null=True, blank=True)
    rc_no = models.CharField(max_length=20, null=True, blank=True)
    vehicle_temp_no = models.CharField(max_length=20, null=True, blank=True)
    chasis_no = models.CharField(max_length=20, null=True, blank=True)
    permit_type = models.CharField(max_length=20, null=True, blank=True)
    road_tax = models.CharField(max_length=20, null=True, blank=True)
    road_tax_expiry = models.DateField(null=True, blank=True)
    fitness = models.CharField(max_length=20, null=True, blank=True)
    fitness_expiry = models.DateField(null=True, blank=True)
    insurance = models.CharField(max_length=20, null=True, blank=True)
    insurance_expiry = models.DateField( null=True, blank=True)
    pollution = models.CharField(max_length=20, null=True, blank=True)
    pollution_expiry = models.DateField(null=True, blank=True)
    permit = models.CharField(max_length=20, null=True, blank=True)
    permit_expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    status_change_date = models.DateField(null=True, blank=True)
    vehicle_onwer = models.CharField(max_length=50, null=True, blank=True)
    onwer_contact = models.CharField(max_length=20, null=True, blank=True)
    onwer_address = models.CharField(max_length=50, null=True, blank=True)
    onn_vehicle = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return str(self.vehicle_onwer)