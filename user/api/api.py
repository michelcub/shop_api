from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This class represents a viewset for the User model. It inherits from
    `viewsets.ModelViewSet` which provides default CRUD (Create, Retrieve, Update, Delete)
    operations.

    Attributes:
        queryset (QuerySet): A QuerySet that retrieves all User instances.
        serializer_class (UserSerializer): A serializer class that converts User instances
        into JSON format.

    Methods:
        get_permissions(self): Determines the permissions for each action based on whether
        the action is "create" or not. If it's "create", it allows any user to create a new
        user. Otherwise, it requires the user to be authenticated.

        create(self, request): Creates a new User instance from the request data. If the
        data is valid, it saves the instance and returns a success message with HTTP status
        201 (Created). If the data is invalid, it returns a failure message with HTTP status
        400 (Bad Request).

        retrieve(self, request, pk=None): Retrieves the authenticated user's data and
        returns it in JSON format with HTTP status 200 (OK). If the user is not authenticated,
        it returns a failure message with HTTP status 401 (Unauthorized).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
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
