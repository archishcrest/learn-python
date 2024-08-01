from django.db import models
from django.conf import settings 
from django.utils import timezone

# Create your models here.

class Agent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=True,max_length=250)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,db_column='user_id')
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    deleted_at = models.DateTimeField(null=True)



class AgentQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_id = models.ForeignKey('Agent', on_delete=models.DO_NOTHING,db_column='agent_id')
    question = models.CharField(null=True,max_length=250)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    deleted_at = models.DateTimeField(null=True)


class AgentAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey('AgentQuestions', on_delete=models.DO_NOTHING,db_column='question_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,db_column='user_id')
    answer = models.CharField(null=True,max_length=1000)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    deleted_at = models.DateTimeField(null=True)

class AgentResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer_id = models.ForeignKey('AgentAnswers', on_delete=models.DO_NOTHING,db_column='answer_id')
    ai_response = models.CharField(null=True,max_length=10000)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    deleted_at = models.DateTimeField(null=True)