from django.urls import path, include
from rest_framework import routers

from Banco.apis import CuentaViewSet
from Banco.apis import BeneficiarioViewSet
from Banco.apis import MovimientoViewSet
from Banco.apis import UsuarioViewSet
from Banco.apis import TransferenciaViewSet


router = routers.DefaultRouter()
router.register('cuentas', CuentaViewSet)
router.register('beneficiarios', BeneficiarioViewSet)
router.register('movimientos', MovimientoViewSet)
router.register('transferencias', TransferenciaViewSet)
router.register("auth", UsuarioViewSet, basename='auth')
urlpatterns = [
    path('api-docs/', include(router.urls)),
]