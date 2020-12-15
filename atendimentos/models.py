from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Dado(models.Model):
    atendente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    contatar = models.CharField(max_length=200)
    assunto = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def publish(self):

        self.save()

    def __str__(self):
        return self.nome