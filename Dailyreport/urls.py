from django.urls import path
from .views import VehicleListView, VehicleDetailView, VehicleCreateView, VehicleUpdateView
from .models import Vehicle

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicle/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle_update'),
]
