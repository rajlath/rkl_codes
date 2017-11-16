from sys import stdin, stdout
 
def swap(arr, l_idx, r_idx):
	temp = arr[l_idx]
	arr[l_idx] = arr[r_idx]
	arr[r_idx] = temp
	return arr
	
n = int(stdin.readline())
 
a = [int(s) for s in stdin.readline().split()]
a.insert(0, 0)
 
g = [0] * (n + 1)
 
q = int(stdin.readline())
 
for qi in range(q):
	l, r = map(int, stdin.readline().split())
	
	g[l] += 1
	g[r + 1] -= 1
 
for i in range(1, n + 1):
	g[i] = (g[i] + g[i - 1])
 
for i in range(1, n + 1):
	if g[i] % 2 == 1:
		a = swap(a, i, n - i + 1)
 
a.pop(0)
 
stdout.write(" ".join([str(s) for s in a]))
