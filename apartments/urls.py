from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("properties/", properties, name="properties"),
    path("evergrace/admin/login/", login_u, name="login"),
    path("evergrace/admin/logout/", logout_u, name="logout"),
    path("evergrace/admin/register/", register, name="register"),
    path("p-details/<int:id>/", details, name="details"),
    path("contact-us/", contacts, name="contacts"),
    path("upload/", upload, name="upload"),
    path("site-map/", site_map, name="sitemap"),
    path("meeting/", schedule, name="schedule-meeting"),
    path("administrator/evergrace/e", admin, name="administrator"),
]