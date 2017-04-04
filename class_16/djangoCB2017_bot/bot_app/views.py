from django.shortcuts import render
from django.http import HttpResponse

from credentials import API_KEY

from django.views.decorators.csrf import csrf_exempt
import json
from my_bot import sendMessage


# https://core.telegram.org/bots/api
# https://api.telegram.org/bot<token>/METHOD_NAME

URL = 'https://api.telegram.org/bot'

# Create your views here.
def index(request):
	return HttpResponse("Welcome!!")

@csrf_exempt
def hook(request):

	data = json.loads(request.body)
	
	message = data['message']
	msg = message['text']
	chat_id = message['chat']['id']

	sendMessage(str(chat_id), msg)

	return HttpResponse('')

if __name__ == '__main__':
	pass