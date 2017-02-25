from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from scrape import get_from_hackernews

from models import Book, News, MyForm
import json


def hello(request):
	return render(request, "index.html")

def count(request, pr):
	ctx = {
		'data': pr,
	}
	return render(request, 'index.html', ctx)

@csrf_exempt
def main(request):
	ctx = {}
	return render(request, 'main.html', ctx)


def magic(request):
	return render(request, 'magic.html')


def populate_news(request):
	data = get_from_hackernews()

	for dx in data:
		try:
			n = News.objects.get(headline=dx['news'])
		except:
			n = News(headline=dx['news'], source=dx['url'],
				points=dx['pts'], author=dx['user'])
			n.save()

	response = json.dumps({'data': data})
	return HttpResponse(response)


class MyView(generic.View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello")

	def post(self, request, *args, **kwargs):
		return HttpResponse("POST REQUEST!!!")

def show_news(request):

	data = News.objects.all()
	news = []

	for dx in data:
		news_item = {
			'headline': dx.headline,
			'source': dx.source,
			'pts': dx.points,
			'author': dx.author,
		}
		news.append(news_item)
	ctx = {'data': news}

	if request.method == 'POST':
		frm = MyForm(request.POST)

		if frm.is_valid():
			print frm.cleaned_data
			return redirect('/')

	frm = MyForm()
	ctx['form'] = frm

	return render(request, 'show_news.html', ctx)