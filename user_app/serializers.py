from rest_framework import serializers
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        fields=['id','user','name','phone_number','email']

