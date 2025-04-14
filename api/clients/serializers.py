from rest_framework import serializers

from core.clients import models


class CreateTelegramDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TelegramClient
        fields = ['tg_id', 'username', 'language_code']


class CreateClientSerializer(serializers.ModelSerializer):
    telegram_data = CreateTelegramDataSerializer()

    class Meta:
        model = models.Client
        fields = ['first_name', 'last_name', 'phone_number', 'telegram_data']



    def to_representation(self, instance):
        return ClientInfoSerializer(instance).data


class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'first_name', 'last_name', 'phone_number']
