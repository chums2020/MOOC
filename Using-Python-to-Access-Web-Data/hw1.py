#read through and parse a file with text and numbers. 
#extract all the numbers in the file and compute the sum of the numbers.
#implement in command line: python hw1.py <data_file>
#eg, python hw1.py regex_sum_259891.txt

import re
import sys

data = open(sys.argv[1])

total = 0
for line in data:
	num = re.findall('[0-9]+', line)
	if num != []:
		print num
		for item in num:
			total = total + int(item)

print "The sum of integers is %d" % total

#the most compact way to solve the problem
#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
