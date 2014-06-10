import BigInt
import Sol_Con
import sys

def Garners_Alg(R, A):
# inverses, inverses[j,i] = aj^(-1) mod ai
	inverses = []
	for i in range(len(A)):
		inverses.append([BigInt.BigInt(0)] * len(A))
    	
    	for i in range (len(A)):
    		for j in range (i):
    			invArr = Sol_Con.LinCon (A[j], BigInt.BigInt(1), A[i])  
			inverses[j][i] = invArr[0]
	
	x = [BigInt.BigInt(0)] * len(A)
	for i in range (len(A)):
		x[i] = R[i]
    		for j in range (i):
			x[i] = inverses[j][i] * (x[i] - x[j])
			x[i] = x[i] % A[i];
			if(x[i] < 0):
				x[i] += A[i]
	
	return x

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
	if(Ai < 2):
		print "Mod > 1!"
		sys.exit(-1)
	Ri %= Ai
	if(Ri < 0):
		Ri += Ai
	R[i] = Ri
	A[i] = Ai

#Euler_Function	
i = 0
isSimplePairwise = True
while(i != n and isSimplePairwise):
	j = i + 1
	while j != n and isSimplePairwise:
		if(Sol_Con.GCD(A[i], A[j]) != 1):
				isSimplePairwise = False
		j += 1
	i += 1
	
if not isSimplePairwise:
	print "Mod(Ai) simple pairwise!"
	sys.exit(-1)
	
V = Garners_Alg(R, A)
print "CoefV = ",V
res = BigInt.BigInt(0)
coefAi = BigInt.BigInt(1)

#Answer
for i in range (len(V)):
	res = res + V[i] * coefAi
	coefAi *= A[i]
	
print "X=", res,"(",coefAi, ")"



	