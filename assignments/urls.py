from django.urls import path
from . import views

urlpatterns = [
    path("", views.assignments_list, name="assignments_list"),
    path("<int:device_id>/", views.assignment_detail, name="assignment_detail"),
]
