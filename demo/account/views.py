from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from django_axios.socket import http

@http(['GET'])
def flutterwave_webhook(request, sio):
    return Response({ 'data': 'Fuck' })