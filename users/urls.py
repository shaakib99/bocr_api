from django.urls import path
from .views import RegisterAPI

urlpatterns = [
    path("register", view=RegisterAPI.as_view(), name="users.register"),
]
