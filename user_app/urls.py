from django.urls import path
from .views import CreateAgent, AgentDetail,Get_agents, UpdateDetails
from property_app.views import PropertyUpdateView
urlpatterns=[
    path('agents/',CreateAgent.as_view(), name="agent"),
    path('agents/all/',Get_agents.as_view(),name='agent_list'),
    path("agents/<int:pk>/", AgentDetail.as_view(), name='agent_details'),
    path("property/<int:pk>/", PropertyUpdateView.as_view()),
    path("agents/auth/<int:pk>/",UpdateDetails.as_view(), name="update_details")
]