from django.urls import path, include
from . import views
urlpatterns = [
   
    path('home/', views.home, name="home"),
    path("question/<str:pk>/", views.question, name="question"),

    
]