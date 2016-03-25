import sys
import json
from re import split as rsplit
from pprint import pprint

def byteify(input):
#Reference: Mark Amery
#http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python/13105359#13105359
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

splitlist = " !:;,.?~@\"\'&#/\\"
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

def hw(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary 
	return scores

def hw2(tweet_file, scores):
	for line in tweet_file:
   		tweet = json.loads(line)
   		tweet = byteify(tweet) 
   		if 'text' in tweet.keys():
   			#pprint(tweet['text'])
   			text = tweet['text']
    		tweet_words = split_string(text, splitlist)
    		#pprint(tweet_words)
    		for word in tweet_words:
    			if word in scores.keys():
    				print scores[word]


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = hw(sent_file)
    hw2(tweet_file, scores)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
