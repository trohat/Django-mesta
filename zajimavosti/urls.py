from django.urls import path

from . import views

# router
urlpatterns = [
    path("", views.index),
    path("pocasi/", views.pocasi),
    path("doprava/", views.doprava),
    path("detail/<str:mesto>", views.detail),
    path("seznam", views.seznam)
]
