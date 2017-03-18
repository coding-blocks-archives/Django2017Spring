from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.views import a

def main(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'index.html')