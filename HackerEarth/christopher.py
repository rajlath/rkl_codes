'''
for (int N = 1; N <= number; N++)
    {
        for (int P = 0; P <= number; P++)
        {
            if (ceilf(sqrtf(N+P)) == sqrtf(N+P) && ceilf(sqrtf(P-N)) == sqrtf(P-N))
            {
                cout << left << setw(10) << N << setw(10) << P << setw(10) << P + N << setw(10) << P - N << endl;
            }
        }
    }
'''
from math import ceil,sqrt

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for x in range(n+1):
        for y in range(n+1):
            if ceil(sqrt(x+y)) == sqrt(x + y) and ceil(sqrt(y-x)) == sqrt((y - x)):
                cnt += 1
    print(cnt)