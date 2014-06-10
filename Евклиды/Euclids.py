import BigInt
import sys

def GCD(a, b):
	if (a < b):
		return GCD (b, a)
	if b == 0:
		return a
	r = 1
	while r != 0:
		r = a % b
		a = b
		b = r
	return a
def GCD_ex(a, b):
	if b == 0:
		return a, 1, 0
	if a == 0:
		return b, 1, 0
	
	x1 = BigInt.BigInt(0)
	x2 = BigInt.BigInt(1)
	y1 = BigInt.BigInt(1)
	y2 = BigInt.BigInt(0)
	
	while b != 0:
		q = a / b
		r = a % b
		a = b
		b = r
		
		xx = x2 - x1 * q
		yy = y2 - y1 * q
		x2 = x1
		x1 = xx
		y2 = y1
		y1 = yy
	x = x2
	y = y2

	return a, x, y
	
def GCD_bin(a, b):
	if (a < b):
		return GCD_bin(b, a)
	if(b == 0):
		return a
	g = BigInt.BigInt(1)
	while(a % 2 == 0) and (b % 2 == 0):
		a /= 2
		b /= 2
		g *= 2
	while(a != 0):
		while(a % 2 == 0):
			a /= 2
		while(b % 2 == 0):
			b /= 2
		if(a >= b):
			a -= b
		else:
			b -= a
	d = g * b
	return d


print "Vibirite algoritm:"
print "prostoy Euclid - enter 1"
print "binarny Euclid - enter 2"
print "racshirenny Euclid - enter 3"
choose = BigInt.BigInt(raw_input())
	
	
if choose == 1:
	print "Euclid's algorithm  GCD(a, b) "
	print "Enter a:", 
	a = BigInt.BigInt(raw_input())
	print "Enter b:", 
	b = BigInt.BigInt(raw_input())
	if (a < 0) or (b < 0):
		print "a and b must be positive!"
		sys.exit(-1)
	print "GCD(", a, ",", b, ") = ", GCD(a,b)	

if choose == 2:
	print "Euclid's algorithm  GCD_bin(a, b) "
	print "Enter a:", 
	a = BigInt.BigInt(raw_input())
	print "Enter b:", 
	b = BigInt.BigInt(raw_input())
	if (a < 0) or (b < 0):
		print "a and b must be positive!"
		sys.exit(-1)
	print "GCD_bin(", a, ",", b, ") = ", GCD_bin(a,b)
	
if choose == 3:
	print "Euclid's algorithm  GCD_ex(a, b) "
	print "Enter a:", 
	a = BigInt.BigInt(raw_input())
	print "Enter b:", 
	b = BigInt.BigInt(raw_input())
	if (a < 0) or (b < 0):
		print "a and b must be positive!"
		sys.exit(-1)
	if a > b:
		GCD, x, y = GCD_ex(a, b)
	else:
		GCD, y, x = GCD_ex(b, a)
			
	print "GCD_ex (", a, ",", b, ") =", GCD, "=", x, "*", a, "+", y, "*", b  
if ((choose > 3) or (choose < 1)):
	print"Oshibka vibora algoritma!"
	sys.exit(-1)

	
	
	
	
	