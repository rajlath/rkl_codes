ll ans,test,i,j,num,maxx,minn,total=0;
for(int i=0;i<32;i++)
    total+=(1<<i);
sc1ll(test);
while(test--)
{
    sc1ll(num);
    for(i=0;i<num;i++)
        sc1ll(arr[i]);
    if(num==1) // if there is only one element in the set
    {
        if(pow_2(arr[0])) // check for power of 2
            printf("YES\n");
        else
            printf("NO\n");
        continue;
    }
    bool flag=false;
    for(int i=0;i<32;i++) //check all the positions at which the bit is set.
    {
        ans=total;
        for(int j=0;j<num;j++) 
        {
            if(arr[j]&(1<<i)) // include all those elements whose i'th bit is set
                ans=ans&arr[j];
        }
        if(pow_2(ans))//check for the set contains elements make a power of 2 or not
        {
            flag=true;
            break;
        }
    }
    if(flag==true)
        printf("YES\n");
    else
        printf("NO\n");
}
