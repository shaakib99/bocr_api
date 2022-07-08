from rest_framework.views import APIView
from rest_framework.response import Response
from bocr_api.common.custom_api_view import CustomAPIView


class InitApi(CustomAPIView):

    def get(self, request):
        return Response(data={"message": "hello world!"})
