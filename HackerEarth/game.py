for T in range(int(input())):
         dim=[int(item) for item in input().split()]
         n=dim[0]
         m=dim[1]
         ans=n*(m-1)+m*(n-1)
         print(ans)