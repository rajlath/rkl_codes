for _ in range(int(input())):
    
    noe = int(input())
    arr = [int(x) for x in input().split()]
    
    no_positive = True
    sum_negative= 0
    for i in arr:
        if i <= 0: sum_negative += i
        else:no_positive = False
    if no_positive:
        print(sum_negative)    
    else:
        arr = sorted(arr)
        k    = 0
        flag = 0
        s    = 0
        for i in range(n-1,-1, -1):
            if arr[i] > 0:
                s += a[i]
                k += 1
            else:
                flag = 1
                break  
        ans = s * k + sums 
        if flag == 1:
            for j in range(i, -1, -1):
                k += 1
                s += a[j]
                t1 = s * k
                       
                
        Arrays.sort(a);int k=0;long s=0;flag=0;int i;
              for( i=n-1;i>=0;i--)
              {w
                  if(a[i]>0)
                  {s+=a[i];
                  k++;
                  }
                  else
                  {flag=1;break;}
              }
              long ans=s*k+sum;
              if(flag==1){
                for(int j=i;j>=0  ;j--)
                 {
                    k++;
                    s=s+a[j];
                    long t1=(s)*(k);
                    sum-=a[j];
                    long t2=t1+sum;
                    if(ans<t2)
                    {
                      ans=t2;                    
                    }
                 
                  
                } 
            }
             
              
