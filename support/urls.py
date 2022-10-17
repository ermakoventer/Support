from django.urls import path, include
from rest_framework.routers import SimpleRouter

from support.views import MessageAPIViewSet, SupportAPIViewSet

router = SimpleRouter()
router.register(r'message', MessageAPIViewSet, basename='message')
router.register(r'support', SupportAPIViewSet, basename='support')

urlpatterns = [
    path('api/', include(router.urls)),
]



