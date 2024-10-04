from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            # Permitir acceso sin autenticación para crear usuario
            permission_classes = [AllowAny]
        else:
            # Requerir autenticación para las demás acciones
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("User created is success", status.HTTP_201_CREATED)

        return Response({"msg": "User created is fail"}, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Obtiene el usuario autenticado directamente
        user = request.user

        # Si el usuario no está autenticado, manejarlo según lo necesites
        if not user.is_authenticated:
            return Response(
                {"detail": "User not authenticated"}, status.HTTP_401_UNAUTHORIZED
            )

        # Serializa y devuelve los datos del usuario
        serializer = UserSerializer(user)  # Solo pasa el objeto `user` al serializador
        return Response(serializer.data, status.HTTP_200_OK)
