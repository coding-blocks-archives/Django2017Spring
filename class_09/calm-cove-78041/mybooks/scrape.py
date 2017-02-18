import requests
from bs4 import BeautifulSoup as BS


def get_from_hackernews():
	url = 'https://news.ycombinator.com/'
	r = requests.get(url)

	soup = BS(r.text)

	data = soup.find_all('table', class_='itemlist')
	rows = data[0].find_all('tr')
	# print rows
	data_list = []

	for ix in range(0, 90, 3):
		tg = rows[ix].find_all('a')[1]
		tg1 = rows[ix+1]

		info = dict()

		info['news'] = tg.text
		info['url'] = tg['href']
		info['pts'] = int(tg1.find_all('span')[0].text.split(' ')[0])
		info['user'] = tg1.find_all('a')[0].text
		data_list.append(info)
	return data_list


if __name__ == '__main__':
	data = get_from_hackernews()
	print data