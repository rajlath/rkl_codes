'''
#include<stdio.h>
int palindrome(int n)
{
  int t,r = 0;
  t=n;
  while(t!=0)
  {
    r=r*10;
    r=r+(t%10);
    t=t/10;
  }
  if(r==n)
    return 1;
  else
    return 0;
}

def palindrome(n):
    t = n
    r = 0
    while t != 0:
        r *= 10
        r += (t % 10)
        t //= 10
        if r == n and len(str(r))%2== 0:
            return 1
    return 0


int palindrome(int n)
{
  int t,r = 0;
  t=n;
  while(t!=0)
  {
    r=r*10;
    r=r+(t%10);
    t=t/10;
  }
  if(r==n)
    return 1;
  else
    return 0;
}

int main()
{
  int k,d=0,i;
  scanf("%d",&k);
  i = k + 1;
  while(1)
  {
    d=palindrome(i);
    //printf("%d ", i);
    if(d==1)
      break;
    i++;
  }
  printf("%d",i);
  return 0;
}
'''
def palindrome(n):
    t = n
    r = 0
    while t != 0:
        r *= 10
        r += (t % 10)
        t //= 10
        if r == n :
            return 1
    return 0

for i in range(int(input())):
    k = int(input())
    k-= 1
    while k > 0:
        if len(str(k))%2:
            k -=1
            continue
        if len(set(str(k))) == len(str(k))//2:
            print(k)
            break
        k -= 1




