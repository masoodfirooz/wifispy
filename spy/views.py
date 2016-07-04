from django.shortcuts import render
from django.http import HttpResponse
import json

myStat = 'testing ...'

def home(request):
	global myStat
	if request.method == 'GET':
		return HttpResponse(myStat)
	else: # POST:
		myStat = json.loads(request.body)
