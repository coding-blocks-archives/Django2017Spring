from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from models import User, MyUser, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello(request):
	return render(request, 'index.html')

def apicall(request):
	data = {
		'status': 'success',
		'name': 'New Button',
	}
	return HttpResponse(json.dumps({'data': data}))

def login_page(request):
	frm = LoginForm()
	ctx = {'form': frm}
	return render(request, 'login.html', ctx)

@csrf_exempt
def user_login(request):
	
	resp = {
		'status': ''
	}

	if not request.method == 'POST':
		resp['status'] = 'Y U NO POST REQUEST?'
		return HttpResponse(json.dumps({'data': resp}))

	frm = LoginForm(request.POST)

	if frm.is_valid():
		print 'yes', frm.cleaned_data
		uname = frm.cleaned_data['username']
		ps = frm.cleaned_data['password']

		u = authenticate(username=uname, password=ps)
		print u

		if u:
			if u.is_active:
				login(request, u)
				# ctx = {'user': u}
				resp['status'] = 'success';
				return HttpResponse(json.dumps({'data': resp}))
				# return render(request, 'logged_in.html')#, ctx)
			else:
				resp['status'] = 'Deactivcated account';
				return HttpResponse(json.dumps({'data': resp}))
		else:
			resp['status'] = 'Invalid User!';
			return HttpResponse(json.dumps({'data': resp}))
	
	resp['status'] = 'Invalid Form Data!!';
	return HttpResponse(json.dumps({'data': resp}))

@login_required
def user_logout(request):
	print request.user
	logout(request)
	return redirect('/')

def register(request):
	frm = RegisterForm()
	ctx = {'form': frm}
	return render(request, 'register.html', ctx)

def register_data(request):
	if request.method == 'POST':
		frm = RegisterForm(request.POST)

		if frm.is_valid():
			fdata = frm.cleaned_data
			uname = fdata['username']
			name = fdata['name']
			passwd = fdata['password']
			addr = fdata['address']
			cont = fdata['contact']

			try:
				print uname, passwd
				# usr = User(username=uname, password=passwd)
				usr = User(username=uname)
				usr.set_password(passwd)
				usr.save()
			except:
				return HttpResponse("User already exists!")

			myusr = MyUser(user=usr, name=name, address=addr, contact=cont)
			myusr.save()

			return render(request, 'success_register.html')
		else:
			return redirect('/register')
	else:
		return HttpResponse('Nice Try!')