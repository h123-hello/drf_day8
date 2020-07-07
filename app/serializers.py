from rest_framework import serializers
from rest_framework_jwt.settings import app_settings

from rest_framework.serializers import ModelSerializer
from app.models import Computer
jwt_payload_handler = app_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = app_settings.JWT_ENCODE_HANDLER
class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ("name","price","brand")