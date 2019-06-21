# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):

    def get(self, request, id=0):
        return Response({
            "code": 200,
            "message": "ok",
            "data": "get id: {}".format(id)
        })

    def post(self, request):
        if request.data:
            return Response({
                "code": 200,
                "message": "ok",
                "data": request.data
            })
        else:
            return Response({
                "code": 503,
                "message": "bad request"
            })

    def put(self, request):
        return Response({
            "code": 200,
            "message": "ok",
            "data": request.data
        })

    def delete(self, request):
        return Response({
            "code": 200,
            "message": "ok",
            "data": "delete success"
        })
