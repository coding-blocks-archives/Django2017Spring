from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from models import User, MyUser, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def hello(request):
	return render(request, 'index.html')


def login_page(request):
	frm = LoginForm()
	ctx = {'form': frm}
	return render(request, 'login.html', ctx)

def user_login(request):
	
	if not request.method == 'POST':
		return redirect('/login')

	frm = LoginForm(request.POST)

	if frm.is_valid():
		print 'yes', frm.cleaned_data
		uname = frm.cleaned_data['username']
		ps = frm.cleaned_data['password']

		u = authenticate(username=uname, password=ps)

		if u:
			if u.is_active:
				login(request, u)
				# ctx = {'user': u}
				return render(request, 'logged_in.html')#, ctx)
			else:
				return HttpResponse("User account deactivated")
		else:
			return HttpResponse("Invalid User!")
	
	return redirect('/login')

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
				usr = User(username=uname, password=passwd)
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