from django.urls import path

from meal import views

urlpatterns = [
    path("", views.meals),
]
