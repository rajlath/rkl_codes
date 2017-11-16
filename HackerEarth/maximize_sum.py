'''
nos_of_elements = int(input())
arr = [int(x) for x in input().split()]
lens = nos_of_elements
ans = 0

def adjust(arr, tmp):
	maxIndex = tmp.index(max(tmp))
	if maxIndex==0:
		arr=arr[1:]		
	if maxIndex==1:
		arr=arr[:-1][::-1]
		
	if maxIndex==2:arr=arr[:-2]
	if maxIndex==3:arr=arr[2:][::-1]
	return arr, tmp[maxIndex]

while len(arr) > 0:
	tmp = []
	tmp.append(arr[0])
	tmp.append(arr[-1])	
	if len(arr) > 1:
		tmp.append(arr[-1] * arr[-2])
		tmp.append(arr[0] * arr[1])
	else:
		tmp.append(arr[0])
		tmp.append(arr[0])
		
	arr, elem = adjust(arr, tmp)
		
	ans += elem
	
print(ans)
'''
RI = lambda: map(int, input().split())
 
n = int(input())
a = [int(x) for x in input().split()] + [0]
v = [0] * (n + 10)
for i in range(n):
    v[i + 1] = max(v[i + 1], v[i] + a[i])
    v[i + 2] = max(v[i + 2], v[i] + a[i] * a[i + 1])
print(v)    
print (v[n])
	
		
	
	

