import BigInt
import Euclid_simple
#import from wiki
def Yakoby(a, p):
	if(Euclid_simple.GCD (a, p) != 1):
		return 0
		
	r = BigInt.BigInt(1)
	
	if(a < 0):
		a = -a
		if(p % 4 == 3):
			r = -r
	while(a != 0):
		t = BigInt.BigInt(0)
		while(a % 2 == 0):
			t += 1
			a = a / 2
		if( t % 2 == 1):
			if(( p % 8 == 3) or (p % 8 == 5)):
				r = -r
	
		if((a % 4 == 3) and (p % 4 == 3)):
			r = -r
		c = a
		a = p % c
		p = c
	return r
	
print "Yakobi ( J(a, p) )"
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter p:", 
p = BigInt.BigInt(raw_input())
print "J(", a, ",", p, ") = ", Yakoby(a,p)	