from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('text/', TextPromtAndReturn.as_view(), name='text-promt-and-return'),
]