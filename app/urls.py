from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="app__index"),
    path("contact/", views.contact_form, name="app__contact_form"),
]
