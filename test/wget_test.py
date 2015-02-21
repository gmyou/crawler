# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys
import getopt

def getHtml(url, values, output):
	#url = 'http://kmug.co.kr/board/zboard.php'

	#values = {'id' : 'sale' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req) 
	the_page = response.read()

	# f = open('../resource/KMug.html', 'w')
	f = open(output, 'w')

	f.write(the_page)


# url = 'http://kmug.co.kr/board/zboard.php'
# values = {'id' : 'sale' }
# output = '../resource/KMug.html'

# getHtml(url,  values, output)

def main(argv):
	inputfile = ''
	outputfile = ''
	params = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:p:",["ifile=","ofile=","params="])
	except getopt.GetoptError:
		print 'test.py -i <url> -o <outputfile> -p <params>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <url> -o <outputfile> -p <params>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-p", "--params"):
			params = arg
	print 'Get Url is ', inputfile
	print 'Output file is ', outputfile
	print 'Parameters are ', params

	#TODO split('&') for Mulit Parameters
	p = params.split('=')
	values = {}
	values[p[0]] = p[1]
	print values
	getHtml(inputfile,  values, outputfile)

if __name__ == "__main__":
	 main(sys.argv[1:])	