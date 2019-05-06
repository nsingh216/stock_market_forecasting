#!/usr/bin/python
import sys 
import datetime


smaInterval = int(sys.argv[1])

for line in sys.stdin: 
	date,stock,openPrice,closePrice,lowPrice,highPrice,volume = line.strip().split(',')
	dateD = datetime.datetime.strptime(date.split(' ')[0], '%Y-%m-%d')

	for i in range(0,smaInterval):
		print "%s\t%s\t%s\t%s" % (stock, dateD + datetime.timedelta(days=i),'o',openPrice)
