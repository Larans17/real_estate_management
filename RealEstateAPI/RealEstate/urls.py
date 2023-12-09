from django.urls import path
from RealEstate.views import *


urlpatterns = [
    path('login/',LoginAPI.as_view(),name='login'),
    
    path('post-property/',PostPropertyAPI.as_view()),
    path('getall-property/',PostPropertyAPI.as_view()),
    path('post-unit/',PostUnitsAPI.as_view()),
    path('getall-unit/',PostUnitsAPI.as_view()),
    path('post-tenant/',PostTenantAPI.as_view()),
    path('getall-tenant/',PostTenantAPI.as_view()),
]