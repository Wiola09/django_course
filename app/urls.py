from django.urls import path
from app.views import home, kreiraj_tekst

urlpatterns = [
    path("", home, name="home"),
    path("postovi/kreiraj/", kreiraj_tekst, name="kreiraj_tekst")
]