from django.urls import path
from . import views

urlpatterns = [
    path("", views.getemail),
    path("login/", views.loginview),
    path("sendotp/", views.sendotp),
    path("inputotp/", views.resetpassword),
    path("newpassword/", views.newpassword)
]
