from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from bocr_api.common.custom_api_view import CustomAPIView
from .serializers import RegisterSerializer


class RegisterAPI(CustomAPIView):

    def post(self, request: HttpRequest):
        reg_serializer = RegisterSerializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        reg_serializer.save()

        return Response(data={})
