import sys 
import datetime


smaInterval = sys.argv[1] 

for line in sys.stdin: 
	date,stock,openPrice,closePrice,lowPrice,highPrice = line.strip().split(',')
	dateD = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M')

	for i in range(0,smaInterval):
		print "%s\t%s" % ((stock, dateD + datetime.timedelta(days=i),'o'),openPrice)
		print "%s\t%s" % (stock, dateD + datetime.timedelta(days=i),'c'),closePrice)
		print "%s\t%s" % (stock, dateD + datetime.timedelta(days=i),'l'),lowPrice)
		print "%s\t%s" % (stock, dateD + datetime.timedelta(days=i),'h'),highPrice)


