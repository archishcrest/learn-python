from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.permissions import IsSuperAdmin, IsAdmin, IsCustomer

from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import AgentSerializer, AgentQuestionsSerializer
from .models import *
import json
from utils.geminicls import TextPromtAndReturn
import uuid

def get_question_object(self, pk):
	try:

		return AgentQuestions.objects.get(pk=pk)
	except AgentQuestions.DoesNotExist:
		return None

def get_agent_object(self, pk):
	try:

		return Agent.objects.get(pk=pk)
	except Agent.DoesNotExist:
		return None


def get_question_for_customer_object(self, pk):
	try:

		return AgentQuestions.objects.get(pk=pk)
	except AgentQuestions.DoesNotExist:
		return None

def get_agent_for_customer_object(self, pk,user):
	try:

		return Agent.objects.get(pk=pk,user_id=user)
	except Agent.DoesNotExist:
		return None

class AgentPublicView(APIView):

	def get(self, request, pk=None):

		if pk:

			agent = get_agent_object(self,pk)

			if agent is None:
				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

			serializer = AgentSerializer(agent)

			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			agents = Agent.objects.all()

			if not agents.exists():
				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

			serializer = AgentSerializer(agents, many=True)

			return Response(serializer.data, status=status.HTTP_200_OK)
	

class AgentView(APIView):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated,IsAdmin]

	def post(self, request):

		serializer = AgentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user_id=self.request.user)

		return Response(serializer.data, status=status.HTTP_200_OK)


	def get(self, request, pk=None):

		if pk:

			agent = get_agent_object(self,pk)

			if agent is None:
				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

			serializer = AgentSerializer(agent)

			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			agents = Agent.objects.all()

			if not agents.exists():
				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

			serializer = AgentSerializer(agents, many=True)

			return Response(serializer.data, status=status.HTTP_200_OK)


	def put(self, request, pk):

		agent = get_agent_object(self,pk)

		if agent is None:
			return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

		serializer = AgentSerializer(agent, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data, status=status.HTTP_200_OK)


class AgentQuestionsView(APIView):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated,IsAdmin]

	def post(self, request,agent_id):

		agent = get_agent_object(self,agent_id)

		if agent is None:
			return Response({"message": "agent not found"},status=status.HTTP_404_NOT_FOUND)

		serializer = AgentQuestionsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(agent_id=agent)

		return Response(serializer.data, status=status.HTTP_200_OK)


	def get(self, request, agent_id):

		agent = get_agent_object(self,agent_id)

		if agent is None:
			return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

		try:
			question = AgentQuestions.objects.filter(agent_id=agent)
		except AgentQuestions.DoesNotExist:
			return Response({"message": "Questions not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = AgentQuestionsSerializer(question, many=True)
		
		return Response(serializer.data, status=status.HTTP_200_OK)


	def put(self, request, agent_id,pk):

		agent = get_agent_object(self,agent_id)

		if agent is None:
			return Response({"message": "agent not found"},status=status.HTTP_404_NOT_FOUND)

		question = get_question_object(self,pk)

		if question is None:
			return Response({"message": "question not found"},status=status.HTTP_404_NOT_FOUND)

		serializer = AgentQuestionsSerializer(question, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data, status=status.HTTP_200_OK)


class AgentQuestionAnswersView(APIView):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated,IsAdmin]


	def post(self, request,agent_id):

		# check if same question id exists
		question_ids = [item["question_id"] for item in request.data]

		if len(question_ids) != len(set(question_ids)):
			return Response({"message": "Same question ids multiple times"},status=status.HTTP_400_BAD_REQUEST)

		# Check if all question_ids exist in the database
		existing_question_ids = AgentQuestions.objects.filter(id__in=question_ids, agent_id=agent_id).values_list('id', flat=True)

		if set(question_ids) != set(existing_question_ids):
			return Response({"error": "Some question(s) do not exist"}, status=status.HTTP_400_BAD_REQUEST)

		# Get prompt from agent

		agent = get_agent_object(self,agent_id)

		if agent is None:
			return Response({"message": "agent not found"},status=status.HTTP_404_NOT_FOUND)


		promptTemplate = agent.prompt

		uniqId = str(uuid.uuid4())

		for item in request.data:
			newAnswer = AgentAnswers(
				question_id= get_question_object(self,item["question_id"]),
				user_id=self.request.user,
				agent_id=get_agent_object(self,agent_id),
				answer=item["answer"],
				ans_id=uniqId
				)
			newAnswer.save()
			promptTemplate = promptTemplate.replace("<?>", item["answer"], 1)

		response = TextPromtAndReturn.promptExec(promptTemplate)

		newAgentResponse = AgentResponse(
			user_id=self.request.user,
			agent_id=get_agent_object(self,agent_id),
			ai_response = response,
			ans_id=uniqId
			)

		newAgentResponse.save()

		return Response(response, status=status.HTTP_200_OK)


# class AgentForCustomerView(APIView):

# 	authentication_classes = [JWTAuthentication]
# 	permission_classes = [IsAuthenticated,IsCustomer]

# 	def post(self, request):

# 		serializer = AgentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save(user_id=self.request.user)

# 		return Response(serializer.data, status=status.HTTP_200_OK)


# 	def get(self, request, pk=None):

# 		if pk:

# 			agent = get_agent_for_customer_object(self,pk,self.request.user)

# 			if agent is None:
# 				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

# 			serializer = AgentSerializer(agent)

# 			return Response(serializer.data, status=status.HTTP_200_OK)
# 		else:
# 			agents = Agent.objects.filter(user_id=self.request.user)

# 			if agents is None:
# 				return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

# 			serializer = AgentSerializer(agents, many=True)

# 			return Response(serializer.data, status=status.HTTP_200_OK)


# 	def put(self, request, pk):

# 		agent = get_agent_for_customer_object(self,pk,self.request.user)

# 		if agent is None:
# 			return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

# 		serializer = AgentSerializer(agent, data=request.data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()

# 		return Response(serializer.data, status=status.HTTP_200_OK)


# class AgentQuestionsForCustomerView(APIView):

# 	authentication_classes = [JWTAuthentication]
# 	permission_classes = [IsAuthenticated,IsCustomer]

# 	def post(self, request,agent_id):

# 		agent = get_agent_for_customer_object(self,agent_id,self.request.user)

# 		if agent is None:
# 			return Response({"message": "agent not found"},status=status.HTTP_404_NOT_FOUND)

# 		serializer = AgentQuestionsSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save(agent_id=agent)

# 		return Response(serializer.data, status=status.HTTP_200_OK)


# 	def get(self, request, agent_id):

# 		agent = get_agent_for_customer_object(self,agent_id,self.request.user)

# 		if agent is None:
# 			return Response({"message": "No data found"},status=status.HTTP_404_NOT_FOUND)

# 		try:
# 			question = AgentQuestions.objects.filter(agent_id=agent,user_id=self.request.user)
# 		except AgentQuestions.DoesNotExist:
# 			return Response({"message": "Questions not found"}, status=status.HTTP_404_NOT_FOUND)

# 		serializer = AgentQuestionsSerializer(question, many=True)
		
# 		return Response(serializer.data, status=status.HTTP_200_OK)


# 	def put(self, request, agent_id,pk):

# 		agent = get_agent_for_customer_object(self,pk,self.request.user)

# 		if agent is None:
# 			return Response({"message": "agent not found"},status=status.HTTP_404_NOT_FOUND)

# 		question = get_question_object(self,pk)

# 		if question is None:
# 			return Response({"message": "question not found"},status=status.HTTP_404_NOT_FOUND)

# 		serializer = AgentQuestionsSerializer(question, data=request.data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()

# 		return Response(serializer.data, status=status.HTTP_200_OK)