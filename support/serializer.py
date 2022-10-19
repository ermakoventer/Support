from support.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

        extra_kwargs = {
            'answer_support': {'read_only': True},
            'status': {'read_only': True}
        }


class SupportSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

        extra_kwargs = {
            'title': {'read_only': True},
            'content': {'read_only': True}
        }
