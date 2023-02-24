from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class VehicleReading(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    meter_reading = models.IntegerField()
    work_accomplished = models.TextField()
    oil_used = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_expenses = models.DecimalField(max_digits=10, decimal_places=2)
