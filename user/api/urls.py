from .api import UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),  # Incluye todas las rutas del router
    path('users/me/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
]