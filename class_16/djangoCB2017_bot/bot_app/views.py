from django.shortcuts import render
from django.http import HttpResponse

from credentials import API_KEY

from django.views.decorators.csrf import csrf_exempt
import json
from my_bot import sendMessage
import requests
from wsgiref.util import FileWrapper
import os

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

	sendMessage(str(chat_id), get_video(msg))

	return HttpResponse('')


def get_video(msg):
	import time
	import subprocess
	os.system('youtube-dl ' + msg + ' -x --audio-format mp3')
	time.sleep(10)
	fname = ''
	l = os.listdir('.')
	for lx in l:
		if '.mp3' in lx:
			fname = lx
			break
	return 'https://80e57d9b.ngrok.io/download?name=' + fname

def download(request):
	name = request.GET.get('name')
	l = os.listdir('.')
	print l
	for lx in l:
		if '.mp3' in lx:
			name = lx
			break
	song = FileWrapper(open(name, 'rb'))
	resp =  HttpResponse(song, content_type='audio/mp3')
	resp['Content-Length'] = os.path.getsize(name)
	return resp

def get_gif(msg):
	url = 'http://api.giphy.com/v1/gifs/search?q=' + msg +'&api_key=dc6zaTOxFJmzC'
	r = requests.get(url)
	data = r.json()['data'][0]

	return data['images']['fixed_height']['url']


if __name__ == '__main__':
	pass