# Generated by Django 4.1.13 on 2024-09-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapweb', '0002_site_siteurls_remove_agentquestions_agent_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteurls',
            name='question',
        ),
        migrations.AddField(
            model_name='siteurls',
            name='url',
            field=models.CharField(max_length=1200, null=True),
        ),
    ]