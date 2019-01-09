# Parameter n is an integer
# The function should return a string
lens, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
deq = []
for i in range(1, k):
    while deq and arr[deq[-1]]>= arr[i]:
        deq.pop()
for i in range(lens):
    while i + k < lens and deq and arr[deq[-1]]>= arr[i+k]:
        deq.pop()
        deq.append(i + k)
        if deq[0] == i:
            deq.pop(0)
        if arr[i] > arr[deq[0]]:
            arr[i], arr[deq[0]] = arr[deq[0]], arr[i]
            break
print(*arr)        
        


    
  
    
    
    
