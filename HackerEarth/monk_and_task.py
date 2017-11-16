"""
t= int(raw_input())
for i in range(t):
    n = int(raw_input())
    print" ".join(map(str,sorted(map(int,raw_input().split(" ")), key=lambda x: bin(x)[2:].count("1"))))
    
for _ in xrange(int(raw_input())) :
    N = int(raw_input())
    A = map(int, raw_input().strip().split(' '))
    A.sort(key = lambda x : bin(x).count('1'))
    print ' '.join(map(str,A))
    
        def sorting(x):
    c=str(bin(x))
    return c.count('1')
a=input()
for i in range(a):
    n=input()
    arr=map(int,raw_input().split())
    arr.sort(key=sorting)
    for j in arr:
        print j,
    print
    
def get_bit(number):
    count = 0
    while number > 0:
        count += 1
        number &= (number - 1)
    return count
 
 
def main():
    t = int(raw_input())
    for i in range(t):
        n = raw_input()
        arr = map(int, raw_input().split())
        for j in range(len(arr)):
            bit = get_bit(arr[j])
            arr[j] = arr[j], bit
        arr = sorted(arr, key=lambda x: x[1])
        for j in range(len(arr)):
            print arr[j][0],
        print('\n')
 
main()

t = int(raw_input())
for x in range(t):
    raw_input()
    countnums = {}
    nums = list(map(int, raw_input().split()))
    for num in nums:
        length = str(bin(num)).count('1')
        #print length
        if countnums.has_key(length):
            countnums[length].append(num)
        else:
            countnums[length] = [num]
    
    string = ''
    #print countnums
    mergedlist = []
    for i in range(1,43):
        if countnums.has_key(i):
            #print ''.join(countnums[i])
            #string += ' '.join(countnums[i])
            mergedlist += countnums[i]
            #print ''.join(mergedlist)
    for elem in mergedlist:
        string += ' ' + str(elem)
    print string[1:] 
       """
for _  in range(int(input()))       :
    input()
    print(" ".join(map(str,sorted(map(int,input().split(" ")), key=lambda x: bin(x)[2:].count("1")))))

