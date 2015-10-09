import mechanize
import cookielib
import requests

from bs4 import BeautifulSoup
from urllib import urlretrieve
from urllib2 import urlopen
from os.path import exists, isfile
import os
from os import makedirs

#############################
#using mechanize


br = mechanize.Browser()
cj=cookielib.LWPCookieJar()
br.set_cookiejar(cj)

#url=raw_input('Download manga from: ')

br.set_handle_robots(False)
br.set_handle_referer(False)
br.set_handle_refresh(False)

br.addheaders = [('User-agent', 'Firefox')]

#br.open(url)
r = br.open('http://anime.thehylia.com/soundtracks/album/code-geass-r2-original-soundtrack-1')
l2 = list(br.links())
#l1 = list(br.find_link(text='Download'))

for l in l2[-24:]:
	br.follow_link(l)
	l3 = br.find_link(text='Download to Computer')
	x1 = (str(l3.url)).rfind('/')
	filename = str(l3.url)[x1+1:]
	filename1 = filename.replace('%20',' ')
	if os.path.isfile(filename1)==False:
		br.retrieve(l3.url,filename1)

#br.follow_link(l1)

print (br.geturl())
################################
#using bs4

# page = requests.get('http://downloads.khinsider.com/game-soundtracks/album/fate-zero-ost').text
# soup1 = BeautifulSoup(page)
# soup2 =  soup1.find_all('tbody')
# chapterlist = []
# for link in soup2[-1].find_all('a'):
# 	print (link.get('href'))
# 	#chapterlist.append((link.get('href')))
# #print chapterlist[:]