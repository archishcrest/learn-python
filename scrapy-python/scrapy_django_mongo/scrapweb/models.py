from django.db import models
from django.conf import settings 
from django.utils import timezone

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()


class SiteUrls(models.Model):
    id = models.BigAutoField(primary_key=True)
    site_id = models.ForeignKey('Site', on_delete=models.DO_NOTHING, db_column='site_id')
    site_page = models.CharField(null=True,max_length=1200)
    url = models.CharField(null=True,max_length=1200)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()

class SiteContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    site_id = models.ForeignKey('Site', on_delete=models.DO_NOTHING, db_column='site_id')
    site_page_id = models.CharField(null=True,max_length=1200)
    content = models.JSONField(null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = ActiveManager()    