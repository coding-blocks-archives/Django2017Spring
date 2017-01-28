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
	<br>

	<form action="/data/add/" method="GET">
	<input type='text' name='one' placeholder='12'><br>
	<input type='text' name='two' placeholder='32'><br>
	<button type='submit'>ADD</button>
	</form>

	</body>

	</html>
	"""

	return HttpResponse(data)


def add(request):
	try:
		one = int(request.GET.get('one', 1))
		two = int(request.GET.get('two', 1))
	except:
		one = 1
		two = 1

	data = """
	<html>
	<head>
	<title>My Page</title>
	</head>

	<body>
	<p align='center'>Welcome Again!!</p>
	<hr>
	The sum is: """ + str(one + two) + """
	<br>

	Click <a href='/data/'>here</a> to go back!

	</body>

	</html>
	"""

	return HttpResponse(data)

def templating(request):
	return render(request, 'main.html')