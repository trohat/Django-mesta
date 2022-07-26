from django.urls import path

from . import views

# router
urlpatterns = [
    path("", views.index, name="index"),
    path("pocasi/", views.pocasi, name="pocasi"),
    path("doprava/", views.doprava, name="doprava"),
    path("detail/<str:mesto>", views.detail, name="detail"),
    path("seznam", views.seznam, name="seznam")
]
