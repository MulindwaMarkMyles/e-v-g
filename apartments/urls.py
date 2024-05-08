from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("properties/", properties, name="properties"),
    path("p-details/<int:id>/", details, name="details"),
    path("contact-us/", contacts, name="contacts"),
    path("upload/", upload, name="upload")
]