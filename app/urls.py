from app import views
from django.urls import path
urlpatterns = [
    path("computers/",views.ComputerListAPIGView.as_view()),
]