# models.py
from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    nic_number = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.card_holder_name

class Parking(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('van', 'Van'),
    ]
    LOCATIONS = [
        ('A1', 'Block A - Level 1'),
        ('A2', 'Block A - Level 2'),
        ('B1', 'Block B - Level 1'),
        ('B2', 'Block B - Level 2'),
    ]

    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    check_in_time = models.DateTimeField()
    duration = models.IntegerField()
    preferred_location = models.CharField(max_length=20, choices=LOCATIONS)

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_type}"