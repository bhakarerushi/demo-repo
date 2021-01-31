from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def first_api(request):
    return Response({'message':'this is demo message for rest api'})


def first_django_view(request):
    return HttpResponse('This is demo massage for django view')


class SecondApi(APIView):

    def get(self, request, *args, **kwargs):
        print(request.query_params)
        print(request.data)
        f = request.query_params.get('xyz')
        z = request.query_params.get('pqr')
        print(f,z)
        return Response({'message':'this is second api'})

    def post(self, request, *args, **kwargs):
        print(request.data,request.query_params)
        return Response({'message':'this is second api'})