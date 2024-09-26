from django.urls import path
from .views import ScrapView

urlpatterns = [
    path('site/', ScrapView.as_view(), name='site'),
]