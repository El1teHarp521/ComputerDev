from django.urls import path
from . import views

urlpatterns = [
    path("", views.devices_list, name="devices_list"),
    path("<int:device_id>/", views.device_detail, name="device_detail"),
]
