#Retrieve layers of URLs
import urllib
from BeautifulSoup import *

n = 8 #number of layers 
url = 'http://python-data.dr-chuck.net/known_by_Elaf.html' #seed
print url

for i in range(1,n): 	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

# Retrieve anchor tag at position 17
	tag = soup('a')[17]
	url = tag['href'].encode('utf-8')
	print url
