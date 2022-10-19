from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from support.models import Message
from support.serializer import MessageSerializer, SupportSerializer
from support.tasks import send_status_message


class MessageAPIViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(sender=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        super(MessageAPIViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('support-list'))


class SupportAPIViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = SupportSerializer
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        """Переопределяем метод update, и когда статус меняется на Resolved
        отправляем сообщение на почту"""
        response = super(SupportAPIViewSet, self).update(request, *args, **kwargs)
        user = Message.objects.get(pk=self.kwargs['pk'])
        if user.status == "Resolved":
            send_status_message.delay(user.sender.profile.email)
        return Response(status=201)
