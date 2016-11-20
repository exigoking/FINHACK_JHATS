from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .forms import MainappForm,CreateRoomForm

def home(requests):
	return render(requests,'index.html',{})

@csrf_exempt
def get_info(requests):
	context={}
	if request.method == "POST":
		
		params=json.loads(requests.body.decode('utf-8'))
		phoneNumber = None
		phoneNumber = params['phoneNumber']
		context['phoneNumber'] = phoneNumber
		
		return HttpResponse(json.dumps(context), content_type='application/json')

	return render(requests,'initial.html',context)


def create_room(requests):
	form = CreateRoomForm(requests.POST or None )
	
	if form.is_valid():
		instance = form.save(commit = False)
		return HttpResponse('Next step for room ')

	context = {
		'form' : form
	}
	return render(requests,'create_room.html',context)

def invite(requests):

	form  = MainappForm(requests.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		return HttpResponse('Next step ')

	context = {
		'form' : form
	}

	return render(requests,'invite.html',context)
