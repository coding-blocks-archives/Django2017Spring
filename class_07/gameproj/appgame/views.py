from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import UserData, GameData

def testing(request):
	return HttpResponse("Working...")


def home(request):
	ctx = {}
	msg = request.GET.get('msg')
	if not msg == None:
		ctx['msg'] = msg

	return render(request, 'index.html', ctx)


def playGame(request):

	uname = request.GET.get('uname')
	ctx = {
		'user': uname
	}
	if uname == None:
		return redirect('/?msg="An error occured! Login Again"')

	return render(request, 'game.html', ctx)


def gameScore(request):

	uname = request.GET.get('uname')
	score = request.GET.get('score')
	gid = request.GET.get('gameid')

	usr = UserData.objects.filter(username=uname)[0]

	game = GameData(user=usr, game_score=int(score), game_id=gid)
	game.save()

	return redirect('/?msg="Score saved. Please login again"')


def leaderBoard(request):

	uname = request.GET.get('uname')

	board_data = []

	for user in UserData.objects.all():
		games = GameData.objects.filter(user=user)
		best_game = sorted(games, key=lambda x: x.game_score, reverse=True)[0]
		new_score_data = {
			'username': user.username,
			'game_id': best_game.game_id,
			'score': best_game.game_score,
			'rank': 0,
		}
		board_data.append(new_score_data)
	board_data = sorted(board_data, key=lambda x: x['score'], reverse=True)
	for ix in range(len(board_data)):
		board_data[ix]['rank'] = ix+1

	ctx = {
		'user': uname,
		'leaders': board_data,
	}

	return render(request, 'leaderboard.html', ctx)


def myPage(request):

	utype = request.GET.get('usertype')
	uname = request.GET.get('uname')
	key = request.GET.get('key')

	ctx = {}

	if utype == None:
		return redirect('/?msg="Error! Please Try again!"')
	elif utype.lower() == 'new':
		try:
			usr = UserData(username=uname, user_key=key)
			usr.save()

			ctx['user'] = usr.username
		
		except:
			return redirect('/?msg="Username Taken! Please use a different one!"')
	elif utype.lower() == 'old':
		users = UserData.objects.filter(username=uname, user_key=key)
		if len(users) > 0:
			usr = users[0]
		
			ctx['user'] = usr.username
			game_data = GameData.objects.filter(user=usr)
			ctx['data'] = {}

			if len(game_data) > 0:
				ctx['data']['played'] = len(game_data)
				ctx['data']['table'] = []

				for gx in game_data:
					new_data = {}
					new_data['id'] = gx.id
					new_data['game_id'] = gx.game_id
					new_data['score'] = gx.game_score
					ctx['data']['table'].append(new_data)

			else:
				ctx['data']['played'] = 0
		
		else:
			return redirect('/?msg="You take me for a fool?"')
	else:
		return redirect('/?msg="What are you trying to do user?"')

	return render(request, 'yourpage.html', ctx)