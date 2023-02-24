from django.shortcuts import render, get_object_or_404


from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Vehicle, VehicleReading

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['name', 'make', 'model']

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['name', 'make', 'model']

class VehicleListView(ListView):
    model = Vehicle
    ordering = ['name']

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleReadingCreateView(CreateView):
    model = VehicleReading
    fields = ['vehicle', 'date', 'meter_reading', 'work_accomplished', 'oil_used', 'maintenance_expenses']

class VehicleReadingUpdateView(UpdateView):
    model = VehicleReading
    fields = ['vehicle', 'date', 'meter_reading', 'work_accomplished', 'oil_used', 'maintenance_expenses']

class VehicleReadingListView(ListView):
    model = VehicleReading
    ordering = ['-date']

class VehicleReadingDetailView(DetailView):
    model = VehicleReading

