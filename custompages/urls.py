from django.urls import path

from . import views


urlpatterns = [
    path('about/', views.about, name="about"),
    path('contacto/', views.contact, name="contact"),
    path('thank-you/', views.thank_you, name="thank_you"),
]
