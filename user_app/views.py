from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins,permissions
from .serializers import AgentSerializer
from .models import Agent
from django.http import Http404
from rest_framework.permissions import IsAuthenticated,AllowAny


class IsAgent(permissions.BasePermission):
    """
    Global permission check for if user is Agent.
    """

    def has_permission(self, request, view):
        user_id = request.user.id  #
        blocked = Agent.objects.filter(user=user_id).exists()
        return blocked

# Create agent account (Authenticated)
class CreateAgent(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer=AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgentDetail(APIView):
    permission_classes=[IsAgent]
    def get_agent(self, id):
        try:
            item=Agent.objects.filter(id=id)
            return item
        except:
            return Http404

    def get(self,request, pk):
        agent = self.get_agent(id=pk)
        serializer = AgentSerializer(agent, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def put(self,request, pk):
    #     agent = self.get_agent(id=pk)
    #     serializer=AgentSerializer(agent, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     agent=self.get_agent(id=pk)
    #     agent.delete()
    #     return Response("Deleted", status=status.HTTP_204_NO_CONTENT)


class Get_agents(generics.ListAPIView):
    permission_classes=[AllowAny]
    serializer_class=AgentSerializer
    queryset=Agent.objects.all()



