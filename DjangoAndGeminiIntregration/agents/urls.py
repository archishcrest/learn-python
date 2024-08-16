# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AgentView, AgentQuestionsView,AgentQuestionAnswersView

urlpatterns = [
    path('agent/', AgentView.as_view(), name='agent'),
    path('agent/<int:pk>/', AgentView.as_view(), name='agent-detail'),
    path('<int:agent_id>/question/', AgentQuestionsView.as_view(), name='agent-question'),
    path('<int:agent_id>/question/<int:pk>', AgentQuestionsView.as_view(), name='agent-question'),
    path('<int:agent_id>/answer', AgentQuestionAnswersView.as_view(), name='agent-answers'),
    # path('question/', MyTokenObtainPairView.as_view(), name='question'),
    # path('answer/', TokenRefreshView.as_view(), name='answer'),
]
