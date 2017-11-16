from math import ceil,log

def get_mid(s, e):
    return s + (e-s)//2
    

           
def update_helper(st, ss, se, i, diff, si):
    if i < ss or i > se: return
    st[si] = st[si] + diff
    if se != ss:
        mid = get_mid(ss, se)
        update_helper(st, ss, mid, i, diff, 2*si+1)
        update_helper(st, mid+1, se, i, diff, s*si+2)
        
def update_value(arr, st, n, i, new_val):
    if i < 0 or i > n-1:
        print("Invalid input")        
        return
    diff = new_val - arr[i]
    arr[i] = new_val
    update_helper(st, 0, n-1, i, diff, 0) 
    
def get_sum(st, n, qs, qe):
    if qs == 0 or qe > n -1 or qs > qe:
        print("invalid Input")
        return 
    return get_sum_helper(st, 0, n-1, qs, qe, 0)  
    
def get_sum_helper(st, ss, se, qs, qe, si):
    if qs <= ss and qe >= se: return
    mid = get_mid(ss, se)
    return (get_sum_helper(st, ss, mid, qs, qe, 2 *si + 1) +
           get_sum_helper(st, mid+1, se, qs, qe, 2 * si + 2)) 
    

           


    
def build_segment_tree(arr,ss,se, st, si):
    if ss == se:
        st[si] = arr[ss]
        return arr[ss]
    mid = get_mid(ss, se)
    st[si] =  (build_segment_tree(arr, ss, mid, st, si*2+1) +
               build_segment_tree(arr, mid+1, se, st, si*2+2))
    return st[si]
    
def create_segment_tree(arr, n):
    tree_height = int(ceil(log(n, 2)))
    tree_size   = 2 * int(pow(2,tree_height)) - 1
    st = [0]*tree_size
    build_segment_tree(arr, 0, n-1, st, 0)
    
    

noe, noq = [int(x) for x in input().split()]  
arr   = [int(x) for x in input().split()]
st = create_segment_tree(arr, noe)
for i in range(noq):
    a, b, c = [int(x) for x in input().split()]
    if a == 1:
        update_value(arr, st, noe, c, b)
    if a == 2:
        print(getSum(st, noe, b, c))
     
    
 
