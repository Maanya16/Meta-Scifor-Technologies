from django.urls import path
from .import views

urlpatterns = [
     path("home/", views.hello, name="home"),
    path("pdf/", views.pdf_to_txt, name="pdf"),
    path("read/", views.ReadPdf, name="read"),

]
