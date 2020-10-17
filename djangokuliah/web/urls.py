from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tugas2', views.tugas2, name="tugas2"),
]