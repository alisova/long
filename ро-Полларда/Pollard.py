import BigInt
import Sol_Con
import sys
#import from wiki
#import from S. p.54

def TrialDivision(n):
	if(n < 0):
		n = -n
	i = 2
	while(i <= (n+1)/2):
		if(n % i == 0):
			return i
		i += 1
	return 1

def new_xab(x, a, b, n, N, alpha, beta):
	c = x % 3
	if(c == 0):
		x = (x*x) % N
		a = (a*2) % n 
		b = (b*2) % n
	elif(c == 1):
		x = x*alpha % N
		a = (a+1) % n
	elif(c == 2):
		x = x*beta % N
		b = (b+1) % n

	return x, a, b 

def RhoPollard(alpha, beta, N):
	n = N - 1
	x = BigInt.BigInt(1)
	a = BigInt.BigInt(0)
	b = BigInt.BigInt(0)
	X = x
	A = a
	B = b
	
	i = BigInt.BigInt(1)
	while(i < n):
		x, a, b = new_xab( x, a, b, n, N, alpha, beta )
		X, A, B = new_xab( X, A, B, n, N, alpha, beta )
		X, A, B = new_xab( X, A, B, n, N, alpha, beta )
		i += 1
		if( x == X and i > 2):
			if (B - b) == 0:
				return None
			Bb = B - b
			Aa = A - a
			if Bb < 0:
				Bb = b - B
			if Aa < 0:
				Aa = a - A
				
			res = Sol_Con.LinCon(Bb, Aa, n)
			if(res == -1):
				return -1
			if(res == -2):
				return -2
			else:	
				return res[0]
			

print "a^x = b mod m"
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
print "Enter m:", 
m = BigInt.BigInt(raw_input())

if(TrialDivision(m) != 1):
	print "m must be prime!"
	sys.exit(-1)
	
print a, "^ x =", b, "mod", m
x = RhoPollard(a, b, m)
if((x == -1 ) or (x == -2)):
	print "No solution"
else:
	print "x = ", x

	