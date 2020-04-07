from rest_framework import viewsets

from .serializers import TicketSerializer
from .models import Ticket


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('name')
    serializer_class = TicketSerializer