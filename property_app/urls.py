from django.urls import path,include
from property_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'PropertyImage', views.YourModelViewSet)

urlpatterns=[
    path('all/',views.PropertyView.as_view(),name="properties"),
    path('<int:pk>/',views.PropertyDetailView.as_view(), name="property_detail"),
    path('agent/<int:pk>/',views.AgentProperty.as_view(),name='agent_property'),
    path('search/',views.PropertySearchView.as_view(), name='property_search'),
    path('detail/<int:pk>/',views.FullDetails.as_view(),name="full_details"),
    path('images/<int:pk>/',views.RetrievePropertyimage.as_view(),name="property_images"),
    path('image/',views.GetPropertyImage.as_view(),name='image'),
    path('api/', include(router.urls)),

]



