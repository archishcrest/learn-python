from django.urls import path
from .views import *

urlpatterns = [
    path('', generateImage.as_view(), name='business-by-category')
]