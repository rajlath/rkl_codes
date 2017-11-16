for _ in range(int(input())):
    input()
    arr =[int(x) for x in input().split()]
    cnt = arr.count(min(arr))
    
    print ("Lucky" if cnt&1 else "Unlucky")
