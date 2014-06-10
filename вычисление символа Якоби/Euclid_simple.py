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

	
	
	
	