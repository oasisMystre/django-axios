from django.urls import path

from .views import flutterwave_webhook

urlpatterns = [
    path(r'flutterwave/', flutterwave_webhook)
]