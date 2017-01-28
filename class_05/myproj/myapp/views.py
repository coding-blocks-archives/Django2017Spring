from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):

	name = request.GET.get('name', "No Name")
	# name = "Shubham"

	data = """
	<html>
	<head>
	<title>My Page</title>
	</head>

	<body>
	<p align='center'>Welcome """ + name + """!!</p>
	<hr>
	This is my page!
	</body>

	</html>
	"""

	return HttpResponse(data)