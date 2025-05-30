from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Banco.apis import UsuarioSerializer
from Banco.models.cuenta_model import Cuenta


class CuentaSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='usuario',
        write_only=True
    )
    usuario = UsuarioSerializer(
        read_only=True,
        many=False
    )


    class Meta:
        model = Cuenta
        fields = '__all__'


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cuenta.objects.filter(usuario=user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def all_accounts(self, request):

        serializer = self.get_serializer(Cuenta.objects.all(), many=True)
        return Response(serializer.data)

