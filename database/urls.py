from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('devices', views.devices, name="devices"),
    path('groups', views.groups, name="groups"),
    path('configs', views.configs, name="configs"),
    path('tools', views.tools, name="tools"),
    path('settings', views.settings, name="settings"),
    path('addDevice', views.addDevice, name="addDevice"), 
]