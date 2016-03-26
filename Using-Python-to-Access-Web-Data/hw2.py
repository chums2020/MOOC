#retrieve HTTP Response headers

#Method 1: use socket

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()


#Method 2: use urllib
import urllib

address = 'http://www.pythonlearn.com/code/intro-short.txt'    
data = urllib.urlopen(address)
print data.headers


#Method 3: command line telnet
$telnet http://www.pythonlearn.com 80
$GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0


