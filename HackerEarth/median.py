import heapq
for _ in range(int(input())):
	lens = int(input())
	arrA = [int(x) for x in input().split()]
	arrB = [int(x) for x in input().split()]
	heapq.heapify(arrA)
	heapq.heapify(arrB)
	cnt = 0
	while arrA[lens//2] != arrB[lens//2]:
		a = heapq.heappop(arrA)
		b = arrB.pop()
		print(a, b, arrA, arrB)
		heapq.heappush(arrA, b)
		heapq.heappush(arrB, a)
		
		cnt += 1
	print(cnt)
		
