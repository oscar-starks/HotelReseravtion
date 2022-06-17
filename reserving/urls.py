from . import views
from django.urls import path

urlpatterns = [
    path("", views.reserveview),
    path("login/", views.loginview),
    path('logout/', views.logoutview),
    path("createuser/", views.createuser),
    path("myreservations/",views.myreservations)
]
