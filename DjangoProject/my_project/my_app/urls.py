from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index,name="index"),
    path("a",views.About,name="about"),
    path("c",views.Contact,name="contact")
]