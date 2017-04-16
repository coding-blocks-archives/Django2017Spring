from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.views import a
from models import *
import random


def main(request):
	# print a()*500
	request.session.set_test_cookie()
	return render(request, 'index.html')


def about(request):
	if request.session.test_cookie_worked():
		print '>'*100
		request.session.delete_test_cookie()

	vis = int(request.COOKIES.get('visit', '0'))
	# print "Number of page visits from you:", vis
	resp = render(request, 'index.html', {'visits': vis+1})
	resp.set_cookie('visit', vis+1)
	return resp

def play_quiz(request):
	# user = request.user
	user = MyUser.objects.filter(name='shubham')[0]
	return HttpResponse('hello')


def create_new_quiz(my_quiz, num_questions=1):
	possible_questions = Questions.objects.all()
	n_questions = random.sample(possible_questions, num_questions)

	quiz = {}
	q_ids = ''

	for qst in range(len(n_questions)):

		q_ids += str(n_questions[qst].id)
		q_ids += ','
		answers = Answers.objects.filter(question=n_questions[qst])
		options = []
		for each_ans in answers:
			A = dict({
				'value': each_ans.option,
				'id': each_ans.id,
			})
			options.append(A)

		quiz[qst] = {
			'question': n_questions[qst].question,
			'q_id': n_questions[qst].id,
			'options': options
		}
	my_quiz.questions = q_ids
	return my_quiz, quiz


def generate_quiz(my_quiz):
	# returns a dictionary of questions and corresponding choices
	all_questions = my_quiz.questions

	if all_questions == '':
		return {'status': 'Error'}
	else:
		pass
	q_ids = all_questions.split(',')[:-1]

	n_questions = []
	for q in q_ids:
		qstn = Questions.objects.filter(id=int(q))[0]
		n_questions.append(qstn)

	quiz = {}

	for qst in range(len(n_questions)):

		answers = Answers.objects.filter(question=n_questions[qst])
		options = []
		for each_ans in answers:
			A = dict({
				'value': each_ans.option,
				'id': each_ans.id,
			})
			options.append(A)

		quiz[qst] = {
			'question': n_questions[qst].question,
			'q_id': n_questions[qst].id,
			'options': options
		}

	return quiz