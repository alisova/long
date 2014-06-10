import BigInt
import sys
#import from wiki
	
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
		return  -2
	
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
	
def ChinRemTheorem(R, A):
	M = BigInt.BigInt(1)
	for Ai in A:
		M *= Ai
	
	x = BigInt.BigInt(0)
	for i in range(len(A)):
		Mi = M / A[i]
		invArr = LinCon (Mi, BigInt.BigInt(1), A[i]) 
		MiInv = invArr[0] 
		x = (x + R[i] * Mi * MiInv) % M
		
	return x, M	
	
print "Kitayskaya teorema:"
print "X = R1 (mod A1)"
print "X = R2 (mod A2)"
print ". . ."
print "X = Rn (mod An)"
	
print "Enter n:",
n = int (input())

R = [0] * n
A = [0] * n	
	
for i in range (n):
	print '\nEnter R%d:' % (i + 1),
	Ri = BigInt.BigInt(raw_input())
	print 'Enter A%d:' % (i + 1),
	Ai = BigInt.BigInt(raw_input())
	if Ai < 2:
		print "Mod  > 1!"
		sys.exit(-1)
	Ri %= Ai
	if Ri < 0:
		Ri += Ai
	R[i] = Ri
	A[i] = Ai

#Euler_Function	
i = 0
isSimplePairwise = True
while i != n and isSimplePairwise:
	j = i + 1
	while j != n and isSimplePairwise:
		if GCD(A[i], A[j]) != 1:
				isSimplePairwise = False
		j += 1
	i += 1
	
if not isSimplePairwise:
	print "Mod (Ai)  simple pairwise!"
	sys.exit(-1)
X, M = ChinRemTheorem(R, A)	
print "\nX =", X, "(",M,")"

	