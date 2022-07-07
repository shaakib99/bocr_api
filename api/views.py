from rest_framework.views import APIView
from rest_framework.response import Response
from bocr_api.common.response_renderer import ResponseRenderer


class InitApi(APIView):
    renderer_classes = [ResponseRenderer]

    def get(self, request):
        return Response(data={"message": "hello world!"})
