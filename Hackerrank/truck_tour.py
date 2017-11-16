'''
#include <iostream>
using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    long long tank = 0;
    unsigned int pump =	0;
    for (unsigned int i = 0; i < n; ++i)
        {
        unsigned int liters;
        unsigned int kilometers;
        cin >> liters >> kilometers;
	tank +=	(long long) (unsigned long long) liters -
                (long long) (unsigned long long) kilometers;
        if (tank < 0)
            {
            pump = i + 1;
            tank = 0;
            }
        }
    cout << pump << endl;
}
Sample Input

3
1 5
10 3
3 4
Sample Output

1
'''
tank = 0
pump = 0
for i in range(int(input())):
    arr = [int(x) for x in input().split()]
    tank += arr[0] - arr[1]
    if tank < 0:
        pump = i+1
        tank = 0
print(pump)        
    
