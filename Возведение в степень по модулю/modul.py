import BigInt
import sys

def PowMod(a, b, m):
	a %= m
	res = BigInt.BigInt(1)
	while(b > 0):
		b-=1
		res = (res * a) % m
		
	return res

print "a^b mod m"
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
print "Enter m:", 
m = BigInt.BigInt(raw_input())

if (a < 0) or (b < 0) or (m <= 0):
	print "a and b must be positive!"
	print "Modulus must be > 0"
	sys.exit(-1)
	
print a, "^", b, "mod", m, "=", PowMod(a, b, m)
	