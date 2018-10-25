def m():
    t=int(input())
    while(t>0):
        l1=[]
        l2=[]
        n,m=map(int,input().split())
        for i in range(n):
            a,b=map(int,input().split())
            l1.append(a)
            l2.append(b)
        l1.sort()
        l2.sort()
        q=l2[-1]
        #print(l1)
        #print(l2)
        for i in range(m):
            beg=0
            end=(n-1)
            a=int(input())
            if(a >= q):
                print(-1)
            else:
                while(beg <= end):
                    mid=int((beg+end)/2)
                    #print(mid,"l1[mid]-->",l1[mid],"L2[mid]--->",l2[mid])

                    if(a <l2[mid] and a >= l1[mid]):
                        print(0)
                        break
                    if(a < l1[mid] and mid == 0):
                        print(l1[mid]-a)
                        break
                    if(a >= l2[mid] and a < l1[mid+1]):
                        #print("L1[mid+1",l1[mid+1],a)
                        print(l1[mid+1]-a)

                        break
                    if(a <= l2[mid]):
                        end=mid
                    # print("Upper")
                    elif(a > l2[mid] ):
                        beg=mid+1
                    #  print("Lower")




        t=t-1


m()