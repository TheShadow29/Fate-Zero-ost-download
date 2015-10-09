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
url1 = raw_input('Enter the link of the website: ')
r = br.open(url1)
l2 = list(br.links())
#l1 = list(br.find_link(text='Download'))
x=int(raw_input('No. of tracks in the list: '))
x*=-1
l3 = l2[x:]
start=int(raw_input('Starting no. of the track: '))
end=int(raw_input('Ending no. of the track: '))
for l in l3[start-1:end]:
	br.follow_link(l)
	l3 = br.find_link(text='Download to Computer')
	x1 = (str(l3.url)).rfind('/')
	filename = str(l3.url)[x1+1:]
	filename1 = filename.replace('%20',' ')
	filename2 = filename1.replace('%2C',',')
	if os.path.isfile(filename2)==False:
		br.retrieve(l3.url,filename2)

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