# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AgentView, AgentQuestionsView,AgentQuestionAnswersView, AgentPublicView

urlpatterns = [
    path('agent/', AgentView.as_view(), name='agent'),
    path('agent/<int:pk>/', AgentView.as_view(), name='agent-detail'),
    path('public/agent/', AgentPublicView.as_view(), name='agent-public'),
    path('public/agent/<int:pk>/', AgentPublicView.as_view(), name='agent-detail-public'),
    path('<int:agent_id>/question/', AgentQuestionsView.as_view(), name='agent-question'),
    path('<int:agent_id>/question/<int:pk>', AgentQuestionsView.as_view(), name='agent-question'),
    path('<int:agent_id>/answer', AgentQuestionAnswersView.as_view(), name='agent-answers'),
    # path('customer/agent/', AgentForCustomerView.as_view(), name='agent'),
    # path('customer/agent/<int:pk>/', AgentForCustomerView.as_view(), name='agent-detail'),
    # path('question/', MyTokenObtainPairView.as_view(), name='question'),
    # path('answer/', TokenRefreshView.as_view(), name='answer'),
]
