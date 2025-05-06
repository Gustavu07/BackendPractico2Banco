from django.contrib.auth.models import User
from django.db import models

from Banco.models import Cuenta


class Beneficiario(models.Model):
    nombreCompleto = models.CharField(max_length=100)

    cuenta_beneficiaria = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name='beneficiarios_de'
    )
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='beneficiarios'
    )

    cuenta_propia = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name='propietarios'
    )

    def __str__(self):
        return f"{self.nombreCompleto} - Beneficiario de: {self.cuenta_beneficiaria} - Propietario de: {self.cuenta_propia}"

