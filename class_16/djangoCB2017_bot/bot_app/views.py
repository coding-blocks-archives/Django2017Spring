from django.shortcuts import render
from django.http import HttpResponse

from credentials import API_KEY


# https://core.telegram.org/bots/api
# https://api.telegram.org/bot<token>/METHOD_NAME

URL = 'https://api.telegram.org/bot'

# Create your views here.
def index(request):
	return HttpResponse("Welcome!!")

if __name__ == '__main__':
	pass