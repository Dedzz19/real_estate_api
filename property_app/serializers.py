from rest_framework import serializers
from .models import Property,PropertyImage
from user_app.serializers import AgentSerializer


 
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Property
        fields='__all__'


class ProperyImageSerializer(serializers.ModelSerializer):
    property=PropertySerializer()
    class Meta:
        model=PropertyImage
        fields='__all__'