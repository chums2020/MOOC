#read the XML data from a URL 
#parse and extract the comment counts from the XML data
#compute the sum of the numbers in the file
#the XML data has a structure <comments><comment><a></a>...<count>num</count></comment></comments>

import urllib
import xml.etree.ElementTree as ET

while True:
    address = raw_input('Enter location: ') #prompt for a URL
    if len(address) < 1 : break

    print 'Retrieving', address 
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)
    comment = tree.findall('comments/comment')
    print "Counts:", len(comment)
    sum = 0
    for item in comment:
        sum = sum + int(item.find('count').text)
    print "Sum:", sum
