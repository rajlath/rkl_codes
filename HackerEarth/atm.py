nop = int(input())
hts = [int(x) for x in input().split()]
hts = hts[::-1]
cnt = 1
for i in range(1, nop):
    if hts[i] <= hts[i-1]:continue
    else:cnt += 1
print(cnt)    
'''
int n;
    scanf("%d", &n);
    int a[n];
    for(int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    int cnt = 1;
    for(int i = 1; i < n; i++)
    {
        if(a[i]<=a[i-1])
            continue;
        else
            cnt++;
    }
    printf("%d\n",cnt);
    return 0;
'''    
