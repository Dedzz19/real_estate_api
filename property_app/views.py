from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Property, PropertyImage
from .serializers import PropertySerializer,ProperyImageSerializer
from django.http import Http404
# Create your views here.


class PropertyView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class= PropertySerializer

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Property.objects.all()
     serializer_class= PropertySerializer
     lookup_field="pk"


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