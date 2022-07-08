from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


class ResponseRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        response = {
            "status": "success",
            "code": status_code,
            "data": data,
            "message": None
        }

        if not str(status_code).startswith("2"):
            response["status"] = "error"
            response["message"] = "detail" in data and data["detail"] or data
            del response["data"]

        return super(ResponseRenderer,
                     self).render(response, accepted_media_type,
                                  renderer_context)


class CustomAPIView(APIView):
    renderer_classes = [ResponseRenderer]
