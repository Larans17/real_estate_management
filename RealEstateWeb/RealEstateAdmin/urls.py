from django.urls import path
from RealEstateAdmin.views import *



urlpatterns = [
    path('dashboard/',admin_dashboard,name="dashboard"),
    path('create/<str:page>/',render_page,name="create"),
    path('create-property/',create_property,name="create-property"),
    path('get-object-list/',get_object_list,name="get-object-list"),
    path('create-unit/',create_unit,name="create-unit"),
    path('create-tenant/',create_tenant,name="create-tenant"),
]
