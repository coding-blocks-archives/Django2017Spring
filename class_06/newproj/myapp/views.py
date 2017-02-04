from django.shortcuts import render
from django.http import HttpResponse

def hello(request):

	name = request.GET.get('name', None)

	if not name == None:
		ctx = {
			'name': name
		}
	else:
		ctx = {}

	return render(request, 'main.html', ctx)


def submitName(request):

	name = request.GET.get('name')
	ctx = {
		'name': {
			'str': name,
			'idx': 12221,
		},
		'num': range(10)
	}

	return render(request, 'one.html', ctx)