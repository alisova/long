import BigInt

def LegSymbol(a, p):
	if (a == -1):
		if ((p - 1) / 2) % 2 == 0:
			return 1
		else:
			return -1	
			
	if a == 1:
		return 1
			
	if a < 0:
		return LegSymbol(-1, p) * LegSymbol (-a, p)
	
	a %= p
	
	if a == 0:
		return 1
		
	if a % 2 == 0:
		if ((p*p - 1) / 8) % 2 == 0:
			return LegSymbol (a/2, p)
		else:
			return -1 * LegSymbol (a/2, p)
			
	if a % 4 == 3 and p % 4 == 3: # !((a - 1)/2 * (p - 1)/2 ) % 2 == 0
		return -1 *LegSymbol(p, a)
	else:
		return LegSymbol (p, a)	
	

print " L(a, p)"
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter p:", 
p = BigInt.BigInt(raw_input())
print "L(", a, ",", p, ") = ", LegSymbol(a,p)

	