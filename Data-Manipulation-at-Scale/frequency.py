#Compute Term Frequency
#Each line of output should contain a term, followed by a space, 
#followed by the frequency of that term in the entire file. 
#Implement in command line: python frequency.py output.txt >> part4.txt

import sys
import json
from re import split as rsplit
from pprint import pprint
import 

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def split_string(source, splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1]=output[-1]+char
    return output

splitlist = " !:;,.?~@\"\'&#/\\"
#index is a dictionary

def update_index(text, index):
	tweet_words = split_string(text, splitlist)
	for word in tweet_words:
		if word in index.keys(): 
			index[word]= index[word] + 1  
		else:
			index[word] = 1


def hw2(tweet_file):
	index = {}
	for line in tweet_file:
   		tweet = json.loads(line)
   		tweet = byteify(tweet) 
   		if 'text' in tweet.keys():
   			text = tweet['text']
    		update_index(text, index)
	return index


def main():
	tweet_file = open(sys.argv[1])
	index = hw2(tweet_file)
	index_list = index.items()
	for item in index_list:
		print item[0], item[1]


if __name__ == "__main__":
    # execute only if run as a script
    main()
#http://stackoverflow.com/questions/419163/what-does-if-name-main-do
#https://docs.python.org/2/library/__main__.html
#https://docs.python.org/3/library/__main__.html
#http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
