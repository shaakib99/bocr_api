from django.http import JsonResponse
from django.urls import path
from .views import InitApi

urlpatterns = [
    path('', view=InitApi.as_view()),
]