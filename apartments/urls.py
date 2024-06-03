from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("houses/", houses, name="houses"),
    path("sk-grace/admin/login/", login_u, name="login"),
    path("sk-grace/admin/logout/", logout_u, name="logout"),
    path("sk-grace/admin/register/", register, name="register"),
    path("p-details/<int:id>/", details, name="details"),
    path("contact-us/", contacts, name="contacts"),
    path("upload/", upload, name="upload"),
    path("site-map/", site_map, name="sitemap"),
    path("meeting/", schedule, name="schedule-meeting"),
    path("administrator/sk-grace/e", admin, name="administrator"),
]