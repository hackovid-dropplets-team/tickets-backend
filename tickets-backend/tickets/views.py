from rest_framework import viewsets

from .serializers import TicketSerializer
from .models import Ticket

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('name')
    serializer_class = TicketSerializer


class HelloView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello world'}
        return Response(content)
