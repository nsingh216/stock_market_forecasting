import sys 

lValueA = list() 
lValueB = list() 

smaInterval = sys.argv[1] 
for line in sys.stdin: 
	(key, val) = line.strip().split('\t') 
	vals = val.split(':') 

	lValueA.append(float(vals[0])) 
	lValueB.append(float(vals[1])) 

	if len(lValueA) == smaInterval:
		sumA = 0
		sumB = 0 

	for a in lValueA: 
		sumA += a 

	for b in lValueB: 
		sumB += b 

	sumA = sumA / smaInterval 
	sumB = sumB / smaInterval 

	print "%s\t%.2f\t%.2f" % (key, sumA, sumB)

	del lValueA[0] 
	del lValueB[0]
