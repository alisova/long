import BigInt
import Sol_Con
import sys
#import from mod-py

def TrialDivision(n):
	if(n < 0):
		n = -n
	i = 2
	while(i <= (n+1)/2):
		if(n % i == 0):
			return i
		i += 1
	return 1

def pow(a, b, m):
	a %= m
	res = BigInt.BigInt(1)
	while(b > 0):
		b-=1
		res = (res * a) % m
		
	return res	

def modular_sqrt(a, p):
	if legendre_symbol(a, p) != 1:
		return 0
	elif a == 0:
		return 0
	elif p == 2:
		return p
	elif p % 4 == 3:
		return pow(a, (p + 1) / 4, p)
	b = BigInt.BigInt(2)
	while (legendre_symbol(b,p) == 1):
		b += 1
	
	t = p - 1
	s = BigInt.BigInt(0)
	while(t % 2 == 0):
		t /= 2
		s += 1
	invArr = Sol_Con.LinCon(a, BigInt.BigInt(1), p)
	invA = invArr[0]
	
	c = pow(b, t, p)
	r = pow(a, (t + 1)/2, p)
	i = BigInt.BigInt(1)
	
	while(i < s):
		e = pow(BigInt.BigInt(2), s - i - 1, p)
		d = pow(r*r*invA, e, p)
		if (d == p - 1):
			r = (r*c)% p
		c = (c*c)% p
		i +=1
	res = [r, - r]
	return res
	
					
def legendre_symbol(a, p):
    ls = pow(a, (p - 1)/2, p)
    if ls == p - 1:
        return -1
    return ls
	
print "  x^2 = a mod p "
print "Enter a:",
a = BigInt.BigInt(raw_input())
print "Enter p:",
p = BigInt.BigInt(raw_input())


if(p < 3):
	print "p must be odd prime!"
	sys.exit(-1)

if(TrialDivision(p) != 1):
	print "p must be prime!"
	sys.exit(-1)
	
a = a % p
if(a < 0):
	a += p
if(a == 0):
	print "x = 0"
	sys.exit(-1)

	
print "X= ", modular_sqrt(a, p)

	