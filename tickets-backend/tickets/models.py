from django.db import models
from django.conf import settings


class Ticket(models.Model):
    name = models.CharField(verbose_name='Títol', max_length=60)
    description = models.TextField(
        verbose_name='Descripció', null=True, blank=True)
    published = models.DateTimeField(
        verbose_name='Publicat', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None)
    # voluntary = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_as_voluntary', related_query_name='ticket_as_voluntary', default=None)


class Volunteering(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'ticket']
