from django.urls import path
from .views import  registration_view
urlpatterns = [
    path("", registration_view, name="name")
]
