#!/usr/bin/python
import sys 

averageList = {}

for line in sys.stdin: 
	stock, date, price, val = line.strip().split('\t') 
	key = stock + "::" + date + "::" + price
	averageList.setdefault(key, []).append(float(val))

for k, v in averageList.items():
	stock, date, price = k.split("::")
	avg = sum(v)/len(v)
	print "%s,%s,%s,%s" % (date,stock,price,avg)
