from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('business/', BusinessByCategory.as_view(), name='business-by-category'),
    path('business/<str:state>/', BusinessByCategoryState.as_view(), name='business-by-category-state'),
    path('business/<str:state>/<str:city>/', BusinessByCategoryStateCity.as_view(), name='business-by-category-state-city'),

    path('services/<str:service>', ServiceByCategory.as_view(), name='service-by-category'),
    path('services/<str:service>/<str:state>/', ServiceByStateCategory.as_view(), name='service-by-category-state'),
    
    #re_path(r'^(?:(?P<state>\w+)/)?$', BusinessByCategoryState.as_view(), name='business-by-category-state'),

    #re_path(r'^(?:(?P<state>\w+)/(?P<city>\w+)/)?$', BusinessByCategoryStateCity.as_view(), name='business-by-category-state-city')
]