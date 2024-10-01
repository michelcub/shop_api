from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from ..models import User
from .serializers import UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
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
            return Response('User created is success', status.HTTP_201_CREATED)

        return Response({'msg':'User created is fail'}, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = self.queryset.filter(pk=pk).last()
        if user:
            serializer = UserSerializer(data=user)
            return Response(serializer.data, status.HTTP_200_OK)

        return Response('No exist this user', status.HTTP_404_NOT_FOUND)


