from django.shortcuts import render
from django.http import HttpResponse

from models import MyData

def hello(request):

	name = request.GET.get('name', None)
	organization = request.GET.get('org', None)

	if not name == None:
		obj = MyData(name=name, organization=organization)
		obj.save()
	else:
		pass

	all_data = MyData.objects.all()
	ctx = {
		'show_table': True,
		'data': [],
		'len': len(all_data)
	}

	for dx in range(len(all_data)):
		new_obj = {}
		new_obj['id'] = all_data[dx].id
		new_obj['name'] = all_data[dx].name
		new_obj['score'] = all_data[dx].score
		new_obj['org'] = all_data[dx].organization
		ctx['data'].append(new_obj)

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