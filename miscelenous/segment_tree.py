def build_segement_tree(pos, low, high):
    global tree , arr
    '''
    build a segment tree from an array
    '''
    print(low, pos)
    if low == high:
        tree[pos] = arr[low-1] #finding min in range
        #tree[pos] = arr[high] #finding max in range
        return
    mid = (low + high) // 2
    build_segement_tree(2*pos + 1, low, mid )
    build_segement_tree(2*pos + 2, mid+1, high)
    #finding min in range
    tree[pos] = min(tree[2*pos+1],tree[2*pos+2])
    #find max in range
    #tree[pos] = min(tree[2*pos+1], tree[2*pos+2])

def rangeQuery( tree, pos, low, high, l,  r)    :
    '''
    find min or max in the range l to r
    '''
    if l <= low and r >= high: #total overlap
        return tree[pos]
    if l > high or r < low:    #No overlap
        return 10e12
    mid=(low+high) // 2
    return min(rangeQuery(tree,2*pos+1,low,mid,l,r),rangeQuery(tree,2*pos+2,mid+1,high,l,r)) #partial overlap
    #return max(rangeQuery(tree,2*pos+1,low,mid,l,r),rangeQuery(tree,2*pos+2,mid+1,high,l,r)) #partial overlap

arr = [1,3,5,2,6,7,8]
tree = [0] * (len(arr)* 2+ 2)
build_segement_tree(0,0,len(arr))
print(rangeQuery(tree,0,0,7,2,3))   #min from 3-5
print(rangeQuery(tree,0,0,7,0,7))   #min from 0-5



