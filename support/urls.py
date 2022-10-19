from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
                              TokenObtainPairView,
                              TokenRefreshView,)

from support.views import MessageAPIViewSet, SupportAPIViewSet

router = SimpleRouter()
router.register(r'message', MessageAPIViewSet, basename='message')
router.register(r'support', SupportAPIViewSet, basename='support')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




