from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Agent, AgentQuestions, AgentAnswers, AgentResponse
#from authapp.serializers import OnlyUserNameSerializer

User = get_user_model()

class OnlyUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class OnlyAgentNameSerializer(serializers.ModelSerializer):
    user = OnlyUserNameSerializer(source='user_id', read_only=True)
    
    class Meta:
        model = Agent
        fields = ['name','user']

class AgentSerializer(serializers.ModelSerializer):

	user = serializers.CharField(source='user_id', read_only=True)
	class Meta:
		model = Agent
		fields = ['name', 'prompt', 'user']
    
    # Make title and slug required fields
	name = serializers.CharField(required=True)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.prompt = validated_data.get('prompt', instance.prompt)
		instance.save()
		return instance

	def create(self, validated_data):
		agent = Agent.objects.create(**validated_data)
		return agent


class AgentQuestionsSerializer(serializers.ModelSerializer):

	agent_name = serializers.CharField(source='agent_id.name', read_only=True)
	username = serializers.CharField(source='agent_id.user_id.username', read_only=True)

	class Meta:
		model = AgentQuestions
		fields = ['question', 'agent_name','username']
    
    # Make title and slug required fields
	question = serializers.CharField(required=True)

	def update(self, instance, validated_data):
		instance.question = validated_data.get('question', instance.question)
		instance.save()
		return instance

	def create(self, validated_data):
		agentQuestions = AgentQuestions.objects.create(**validated_data)
		return agentQuestions