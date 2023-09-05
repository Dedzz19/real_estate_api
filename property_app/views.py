from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from .models import Property, PropertyImage
from .serializers import PropertySerializer,ProperyImageSerializer
from django.http import Http404
from user_app.views import IsAgent
from django.contrib.auth.models import User
# Create your views here.

# List Property for Authenticated Users
class PropertyView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class= PropertySerializer

class PropertyDetailView(generics.RetrieveAPIView):
     queryset = Property.objects.all()
     serializer_class= PropertySerializer
     lookup_field="pk"

class PropertyUpdateView(APIView):
    permission_classes=[IsAgent]
    def get_property(self, request, id):
            user=User.objects.get(username=request.user.username)
            item=Property.objects.get(id=id)
            agent=item.agent.user.username
            if agent == user.username:
                return item
            raise Http404
    
    def get(self, request, pk):
        item= self.get_property(request, id=pk)
        serializer=PropertySerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        item= self.get_property(request, id=pk)
        serializer=PropertySerializer(Property,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        item= self.get_property(request, id=pk)
        item.delete()
        return Response("Item deleted successfully", status=status.HTTP_200_OK )

class AgentProperty(APIView):
    def get_agent(self,id):
        try:
            item=Property.objects.filter(agent=id)
            return item
        except:
            raise Http404
    
    def get(self, request, pk):
        items=self.get_agent(id=pk)
        serializer=PropertySerializer(items, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
# Search for property view (Unauthenticated)
class PropertySearchView(APIView):
    def get(self, request):
        location = request.query_params.get('location')
        property_type = request.query_params.get('property_type')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        properties = Property.objects.all()

        if location:
            properties = properties.filter(address__icontains=location)

        if property_type:
            properties = properties.filter(property_type=property_type)

        if min_price:
            properties = properties.filter(price__gte=min_price)

        if max_price:
            properties = properties.filter(price__lte=max_price)

        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# To see the Full profile of a Property (Unauthenticated)
class FullDetails(APIView):
    def get(self,request,pk):
        item =PropertyImage.objects.filter(property=pk)
        serializer=ProperyImageSerializer(item, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
# To see images based on their property id
class RetrievePropertyimage(APIView):
    def get_image(self,id):
        try:
            items = PropertyImage.objects.filter(property__id=id)
            return items
        except:
            raise Http404
    
    def get(self, request, pk):
        items=self.get_image(id=pk)
        serializer=ProperyImageSerializer(items, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class GetPropertyImage(generics.ListAPIView):
    queryset=PropertyImage.objects.all()
    lookup_field='pk'


# Handling pictures

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = ProperyImageSerializer