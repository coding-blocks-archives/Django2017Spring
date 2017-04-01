import requests
import json

url = 'http://www.omdbapi.com/'

data = {
	# 'type': 'movie',
	'r': 'json',
	's': 'Breaking Bad'
}

r = requests.get(url, params=data)

print r.json()