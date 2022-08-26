from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.QuestionView.as_view(), name="question-index")
]