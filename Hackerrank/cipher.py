'''
#include<stdio.h>

int a[1000000];

int main()
{
    int n, k;
    scanf("%d %d\n", &n, &k);
    int head = 0, curr = 0;
    for (int i = 0; i < n; i++)
    {
        if (i - head == k)
            curr ^= a[head++];
        a[i] = (getchar() - '0') ^ curr;
        printf("%d", a[i]);
        curr ^= a[i];
    }
    printf("\n");
    return 0;
}
'''
n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input()]
head = 0
curr = 0
a = [0] * n
for i in range(n):
        if i - head == k:
                curr = curr ^ a[head]
                head += 1
        a[i] = arr[i] ^ curr
        print(a[i], end="")
        curr ^= a[i]

