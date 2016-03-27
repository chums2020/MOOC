#Retrieve layers of URLs
import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Elaf.html'
print url
for i in range(1,8):	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
	tag = soup('a')[17]
	url = tag['href'].encode('utf-8')
	print url
