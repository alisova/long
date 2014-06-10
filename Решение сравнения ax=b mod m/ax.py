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
	
def LinCon (a, b, m):
	d = GCD(a, m)	
	if b % d != 0:
		return -1
	
	if (a == 0 and b % m == 0) or (b == 0 and a % m == 0):
		return -2
	
	a1 = a / d
	b1 = b / d
	m1 = m / d
	d1, x, y = GCD_ex(a1, m1)	
	res0 = ( b1 * x ) % m
	while res0 < 0:
		res0 += m

	resAll = []
	resAll.append(res0)
	d = d - 1
	while d > 0:
		resAll.append( (resAll[-1] + m1) % m )
		if resAll[-1] < 0:
			resAll[-1] += m
		d -= 1
	
	return resAll	
		
print "ax = b mod m"
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
print "Enter m:", 
m = BigInt.BigInt(raw_input())

if (m <= 0):
	print "m must be positive!"
	sys.exit(-1)
	
choose = LinCon(a, b, m)

if(choose == -1):
	print"Comparison",a,"x = ",b,"mod", m,"has no solutions"
	sys.exit(-1)
if(choose == -2):
	print"Comparison",a,"x = ",b,"mod",m,"has a solution x - any"
	sys.exit(-1)
else:
	print"Comparison",a,"x = ",b,"mod", m,"has a solution x = ",choose
	sys.exit(-1)
	
	