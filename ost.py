import mechanize
import cookielib
import requests

from bs4 import BeautifulSoup
from urllib import urlretrieve
from urllib2 import urlopen
from os.path import exists, isfile

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
r = br.open('http://downloads.khinsider.com/game-soundtracks/album/fate-zero-ost')
l2 = list(br.links(text='Download'))
#l1 = list(br.find_link(text='Download'))

for l in l2:
	br.follow_link(l)
	l3 = br.find_link(text='Click here to download')
	filename = str(l3.url)[48:]
	br.retrieve(l3.url,filename)

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