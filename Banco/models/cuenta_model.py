import random

from django.contrib.auth.models import User
from django.db import models


class Cuenta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombreCompleto = models.CharField(max_length=100)
    ci = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=20, unique=True,blank=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.numero_cuenta:
            self.numero_cuenta = self.generar_nro_cuenta()
        super().save(*args, **kwargs)

    def generar_nro_cuenta(self):
        while True:
            nro = str(random.randint(10 ** 9, (10 ** 10) - 1))
            if not Cuenta.objects.filter(numero_cuenta=nro).exists():
                return nro

    def __str__(self):
        return f"{self.nombreCompleto} {self.numero_cuenta} "

