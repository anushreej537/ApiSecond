from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Function based api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

@csrf_exempt
def student_create(request):
 if request.method == 'POST':
  json_data = request.body
  stream = io.BytesIO(json_data)
  pythondata = JSONParser().parse(stream)
  serializer = StudentSerializer(data=pythondata)
  if serializer.is_valid():
   serializer.save()
   res = {'msg': 'Data Created'}
   json_data = JSONRenderer().render(res)
   return HttpResponse(json_data, content_type='application/json')
  json_data = JSONRenderer().render(serializer.errors)
  return HttpResponse(json_data, content_type='application/json')


@api_view(['GET'])
def getdata(request):
 if request.method =='GET':
  obj = Student.objects.all()
  serializer = StudentSerializer(obj,many=True)
  return Response(serializer.data)

@api_view(['POST'])
def senddata(request):
 if request.method == 'POST':
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   res = {'msg':'data created'}
   return Response(status=res.status.HTTP_201_ok)
  return Response(serializer.data)