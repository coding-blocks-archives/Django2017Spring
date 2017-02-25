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


def get_books_goodread():
	base_url = 'https://www.goodreads.com'
	url = base_url + '/shelf/show/fiction'
	r = requests.get(url)

	html = r.text
	soup = BS(html)

	book_links = soup.find_all('a', class_='bookTitle')
	all_books = []
	print len(book_links)
	for lx in book_links:
		print lx
		print '-'*100
		book_url = base_url + lx['href']
		r = requests.get(book_url)

		sp = BS(r.text)

		title = sp.find_all('div', class_='infoBoxRowItem')[0].text
		isbn = sp.find_all('div', class_='infoBoxRowItem')[1].text.split()[0]

		summ = sp.find_all('div', id='description')[0].find_all('span')[1].text
		auth = sp.find_all('a', class_='authorName')[0].span.text

		book_info = {
			'title': title,
			'isbn': isbn,
			'summary': summ,
			'author': auth,
			'img_url': sp.find_all('img', id='coverImage')[0]['src'],
		}
		all_books.append(book_info)
	return all_books


if __name__ == '__main__':
	data = get_from_hackernews()
	print data