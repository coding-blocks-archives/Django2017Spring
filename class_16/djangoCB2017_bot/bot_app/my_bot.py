import requests
from credentials import API_KEY

URL = 'https://api.telegram.org/bot'

def store_offset(offset):
	f = open('offset.txt', 'w')
	f.write(str(offset))
	f.close()

def get_offset():
	f = open('offset.txt', 'r')
	of = f.read().split(' ')[0]
	f.close()
	return of

def verify_bot():
	url = URL + API_KEY + '/getMe'
	r = requests.get(url)
	data = r.json()
	if data['ok']:
		pass
	else:
		print "Bot Error: Unauthorized Access"


def getMessages():

	try:
		off = get_offset()
	except:
		off = 0

	url = URL + API_KEY + '/getUpdates?offset=' + str(off)
	r = requests.get(url)

	data = r.json()
	print data
	for msg in data['result']:
		sendMessage(str(msg['message']['chat']['id']), msg['message']['text'])
		print '---------------------------------'

	if len(data['result'])>0:
		store_offset(str(int(data['result'][-1]['update_id']) + 1))


def sendMessage(chat_id, text=''):
	url = URL + API_KEY + '/sendMessage?chat_id='
	url += chat_id
	url += '&text='
	url += text
	r = requests.get(url)


def init_bot():
	addr = 'https://80e57d9b.ngrok.io/353249793:AAHvZltlXyWwvFj5vRDGGPLq4518npidt7s/'
	url = URL + API_KEY + '/setWebhook?url=' + addr
	r = requests.get(url)
	print r



if __name__ == '__main__':
	# verify_bot()
	# getMessages()

	init_bot()