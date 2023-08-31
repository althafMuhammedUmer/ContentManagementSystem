from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_content, name="create_content"),
    path('content/', views.get_content, name="contents"),
    path('content/<int:id>/', views.get_content, name="get_content"),
    path('content_action/<int:id>/', views.content_actions, name="get_content"),
    
    

]