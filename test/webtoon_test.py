# coding: utf8
import urllib
from bs4 import BeautifulSoup
import os

HOST = 'http://zangsisi.tumblr.com/post/100002577940'
html = urllib.urlopen(HOST)
soup = BeautifulSoup(html)

book = 0
for link in soup.select('div.PostBody p a'):
	print
	print
	print link.get_text()
	print
	page_url = link['href']
	page = urllib.urlopen(page_url)
	soup2 = BeautifulSoup(page)

	book += 1
	str_book = '%0*d' % (3, book)
	print str_book
	print

	chapter = 0

	for d_link in soup2.select('div.PostBody div.wrapper div.image a.zoom'):
		
		print d_link['href']

		image = urllib.URLopener()

		download_path = '/tmp/webtoon/SevenSins/'+str_book
		try:
			os.stat(download_path)
		except:
			os.mkdir(download_path)

		chapter += 1
		str_chapter = '%0*d' % (3, chapter)
		print str_chapter

		download_file = download_path+'/'+str_chapter+'.jpg'
		image.retrieve(d_link['href'], download_file)
