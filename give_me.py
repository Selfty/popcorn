from BeautifulSoup import BeautifulSoup
import urllib2
import re

*****************************

tv.rikrek.cz

https://www.film-serial.cz/serialy/dva-a-pul-chlapa/a1-serie/

def main():

html_page = urllib2.urlopen("http://tv.rikrek.cz/serial/22-vikingove-online/755-s02e01-valka-bratru")
soup = BeautifulSoup(html_page)
links = []
for link in soup.findAll('div', attrs={"class": "episodes"}):
	src = link.findAll('a')
	for a in src:
		links.append('http://tv.rikrek.cz' + a['href'])

for lin in links:
	html_page = urllib2.urlopen(lin)	
	soup = BeautifulSoup(html_page)	
	print soup.find('source')['src']

******************************
film-serial.cz	

html_page = urllib2.urlopen("http://film-serial4.webnode.sk/serialy/south-park/a18-serie/")
soup = BeautifulSoup(html_page)
links = []
for link in soup.findAll('a', attrs={"class": "product-more"}):
	links.append('https://www.film-serial.cz' + link['href'])
	print link['href']

for lin in links:
	html_page = urllib2.urlopen(lin)	
	soup = BeautifulSoup(html_page)	
	print soup.findAll('iframe')[0]['src'].replace("	", "")

*******************************
"""
film-serial.sk
"""


html = urllib2.urlopen('https://www.film-serial.sk/products/american-horror-story/')
soup = BeautifulSoup.BeautifulSoup(html)
soup = soup.find('div', attrs={'class':'wrapperText'})
series = []
for serie in soup.findAll('a'):
	series.append(serie['href'])
	print serie['href']


for page in series:
	html = urllib2.urlopen(page)
	soup = BeautifulSoup.BeautifulSoup(html)
	for episode in soup.findAll('div',attrs={'class':'boxTitle'}):
		html = urllib2.urlopen('https://www.film-serial.sk' + episode.find('a')['href'])
		soup = BeautifulSoup.BeautifulSoup(html)
		print soup.find('iframe')['src'].replace("	","")


