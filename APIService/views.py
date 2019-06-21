from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response

from APIService.models import Person


class Index(APIView):
    def get(self, request):
        return Response({
            "code": 200,
            "message": "ok",
            "data": "get success"
        })

    def post(self, request):
        data = None
        if request.content_type == 'application/json':
            data = request.data
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.POST


        if data:
            return Response({
                "code": 200,
                "message": "ok",
                "data": data
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
            "data": "put success"
        })

    def delete(self, request):
        return Response({
            "code": 200,
            "message": "ok",
            "data": "delete success"
        })
