import sys 

for line in sys.stdin: 
	val = line.strip() 
	vals = val.split(',') 
	print "%s\t%s:%s" % (vals[0], vals[1], vals[2])
