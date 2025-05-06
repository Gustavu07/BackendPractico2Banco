from django.contrib.auth.models import User

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UsuarioViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    @action(methods=['post'], detail=False, url_path='register')
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not password or not email:
            return Response({'error': 'El Username y la contraseña son requeridos'}, 400)
        user = User.objects.create_user(email, email, password)
        return Response({'id': user.id, 'email': user.email}, 201)
