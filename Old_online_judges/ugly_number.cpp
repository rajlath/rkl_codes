'''
Description

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers. By convention, 1 is included.
Given the integer n,write a program to find and print the nth ugly number.
Input

Each line of the input contains a postisive integer n (n <= 1500).Input is terminated by a line with n=0.
Output

For each line, output the n’th ugly number .:Don’t deal with the line with n=0.
Sample Input

1
2
9
0
Sample Output

1
2
10
'''
#include <iostream>
using namespace std;

int main(){

    int DP[1500] = {1}, t2 = 0, t3 = 0, t5 = 0, tmp, i;
	for(i = 1; i < 1500; i++) {
		while(DP[t2]*2 <= DP[i-1])	t2++;
		while(DP[t3]*3 <= DP[i-1])	t3++;
		while(DP[t5]*5 <= DP[i-1])	t5++;
		tmp = DP[t2]*2;
		if(DP[t3]*3 < tmp)	tmp = DP[t3]*3;
		if(DP[t5]*5 < tmp)	tmp = DP[t5]*5;
		DP[i] = tmp;
	}
    for(;;)
    {
        int curr;
        cin >> curr;
        if (curr == 0) break;
        cout <<  DP[curr-1] << "\n";
    }


    return 0;
}