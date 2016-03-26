#Use BeautifulSoup to crawl data
import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_259896.html'
html = urllib.urlopen(url).read()
print html
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
	num = int(tag.getText("span"))
	sum = sum + num
print sum
