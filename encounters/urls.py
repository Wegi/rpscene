from django.urls import path

from . import views

app_name = 'encounters'
urlpatterns = [
    path('npcs/5e/', views.IndexDnD5eNPC.as_view(), name='npc.5e'),
    path('npcs/add/5e/', views.Create5eNPC.as_view(), name='npc.5e.add'),
]
