from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index,name="index"),
    path("a",views.About,name="about"),
    path("co",views.Courses,name="courses"),
    path("p",views.Page,name="page"),
    path("c",views.Contact,name="contact")
]