from django.urls import path
from .views import PropertyView, PropertyDetailView,AgentProperty,PropertySearchView,FullDetails,RetrievePropertyimages,GetPropertyImage
urlpatterns=[
    path('all/',PropertyView.as_view(),name="properties"),
    path('<int:pk>/',PropertyDetailView.as_view(), name="property_detail"),
    path('agent/<int:pk>/',AgentProperty.as_view(),name='agent_property'),
    path('search/',PropertySearchView.as_view(), name='property_search'),
    path('detail/<int:pk>/',FullDetails.as_view(),name="full_details"),
    path('images/<int:pk>/',RetrievePropertyimages.as_view(),name="property_images"),
    path('image/',GetPropertyImage.as_view(),name='image')
]