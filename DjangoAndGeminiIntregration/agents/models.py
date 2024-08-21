from django.db import models
from django.conf import settings 
from django.utils import timezone

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Agent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    prompt = models.CharField(null=True,max_length=10000)
    active = models.BooleanField(default= False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,db_column='user_id')
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()



class AgentQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_id = models.ForeignKey('Agent', on_delete=models.DO_NOTHING, db_column='agent_id')
    question = models.CharField(null=True,max_length=250)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()


class AgentAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey('AgentQuestions', on_delete=models.DO_NOTHING,db_column='question_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,db_column='user_id')
    agent_id = models.ForeignKey('Agent', on_delete=models.DO_NOTHING,db_column='agent_id')
    answer = models.CharField(null=True,max_length=1000)
    ans_id = models.CharField(null=True,max_length=1000)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()

class AgentResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_id = models.ForeignKey('Agent', on_delete=models.DO_NOTHING,db_column='agent_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,db_column='user_id')
    ans_id = models.CharField(null=True,max_length=1000)
    ai_response = models.CharField(null=True,max_length=10000)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()