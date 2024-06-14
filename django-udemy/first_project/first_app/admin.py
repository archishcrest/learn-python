from django.contrib import admin

from first_app.models import Topic, WebPages, AccessRecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(WebPages)
admin.site.register(AccessRecord)