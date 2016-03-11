import os
import urllib

#the url can translate to pirate language

def check_pirate(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
    if output!=text_to_check:
        print('Pirate words detected!')

def read_text():
    os.chdir("/home/yingting/Documents/Udacity/Programming Foundation with Python")
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_pirate(contents_of_file)


read_text()



