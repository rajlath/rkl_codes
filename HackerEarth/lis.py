global maximum
global elem 

def _lis(arr, n):
    global maximum
    global elem
    if n == 1 : return 1
    max_ending_here = 1
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > max_ending_here:
            elem.append(arr[i-1])
            max_ending_here = res + 1
            
    maximum = max(maximum, max_ending_here)
    return max_ending_here
elem = []    
def lis(arr)            :
    global maximum
    global elem
    n = len(arr)
    maximum = 1
    _lis(arr, n)
    
    return maximum
    
print(lis([10,22,9,33,23,21,50,41,60]))    
            
    
