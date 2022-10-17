from support.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        for field in fields:
            fields['answer_support'].read_only = True
            fields['status'].read_only = True
        return fields


class SupportSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields['title'].read_only = True
            fields['content'].read_only = True
        return fields
