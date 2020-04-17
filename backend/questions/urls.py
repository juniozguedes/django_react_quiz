from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all', views.getQuestions, name='getQuestions'), #Get all questions in database
    path('<int:id>', views.getQuestionById, name='getQuestionById'),
]
