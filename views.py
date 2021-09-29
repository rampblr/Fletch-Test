from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
import pandas as pd
import json
from django.http.response import JsonResponse

class CustomerApiView(APIView):
	def get(self,request):
		markList	= pd.DataFrame(list(Customer.objects.all().values()))
		
		return Response({"Cusomter Details":json.loads(markList.to_json(orient='records'))})
	def post(self, request):
		
		data = request.data
		print(type(data))
		if Customer.objects.filter(email=data["email"]).exists():
			
			
			response = JsonResponse({"status":201, "Message":"Email id already registered!!!"})
			response.status_code = 201
			return response
		elif Customer.objects.filter(phone=data["phone"]).exists():
			response = JsonResponse({"status":201, "Message":"Phone number already registered!!!"})
			response.status_code = 201
			return response
		else:
			print('here')
			c = Customer(name=data["name"], email=data["email"], phone=data["phone"])
			c.save()
			
			response = JsonResponse({"status":200, "Message":"Registered Successfully!!!"})
			response.status_code = 200
			return response