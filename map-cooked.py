#!/usr/bin/python
import sys 
import datetime


smaInterval = int(sys.argv[1])

for line in sys.stdin: 
	tokens = line.strip().split(',')
	date = tokens[0]
	openPrice = tokens[4]
	stock = tokens[1]
	dateD = datetime.datetime.strptime(date.split(' ')[0], '%Y-%m-%d')

	for i in range(0,smaInterval):
		print "%s\t%s\t%s\t%s" % (stock, dateD + datetime.timedelta(days=i),'o',openPrice)
