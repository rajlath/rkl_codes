N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
 
modN = 10**9+7
S_1 = 0
S_2 = 0
S_3 = 0
 
for i in range(0, K):
	S_3 = (S_3 + A[i]) % modN
	S_2 = (S_2 + (i+1) * A[i]) % modN
	S_1 = (S_1 + (i+1)**2 * A[i]) % modN
output = []
output.append(S_1)
 
for i in range(0, N-K):
	S_1 = (S_1 + (K+1)**2*A[K+i] - 2*(S_2 + (K+1) * A[K+i]) + S_3 + A[K+i]) % modN
	output.append(S_1)
	S_2 = (S_2 + (K+1)*A[K+i] - (S_3 + A[K+i])) % modN
	S_3 = (S_3 + A[K+i] - A[i]) % modN
	
print( " ".join(map(str, output)))
