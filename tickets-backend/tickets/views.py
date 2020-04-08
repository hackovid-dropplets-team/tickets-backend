from rest_framework import viewsets

from . import serializers
from . import models
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all().order_by('name')
    serializer_class = serializers.TicketSerializer


class VolunteeringViewSet(viewsets.ModelViewSet):
    queryset = models.Volunteering.objects.all()
    serializer_class = serializers.VolunteeringSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class HelloView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello world'}
        return Response(content)
