/*
Expected Dice
Time limit: 1000 ms
Memory limit: 128 MB

You have two special dice with 66 faces, each. For each dice you know the numbers written on each face.

You roll the two dices at the same time, and you add up the numbers showing on the upper faces. What is the most probable sum value you'll get?

Standard input
The first line contains 66 integers representing the numbers on the first dice.

The second line contains 66 integers representing the numbers on the second dice.

Standard output
Print the answer on the first line. If the solution is not unique, print the smallest one.

Constraints and notes
The numbers on the dice are integers between 11 and 5050
Input	Output	Explanation
1 2 3 4 5 6
1 2 3 4 5 6
7
There are 66 ways to roll the dices to make the sum 77.

\{1, 6\}{1,6}, \{2, 5\}{2,5}, \{3, 4\}{3,4}, \{4, 3\}{4,3}, \{5, 1\}{5,1} and \{6, 1\}{6,1}

The other sums have a smaller change to appear. For example, the only way to make 22 is \{1, 1\}{1,1}
1 1 1 1 1 1
1 1 2 2 3 3
2
The first dice will always roll 11, and the second one will roll with the same probability 1, 2\ \text{and}\ 31,2 and 3.

All the sums (2,\ 3,\ 42, 3, 4) have the same chanche to be rolled, so the answer is the lowest one (22)

1 1 1 1 1 1
1 1 2 3 3 3
4
The first dice will always roll 11 but for the second dice, number 33 is more encountered.

This makes sum 44 the most common sum (appearing in 50\%50% or the cases).

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
dice_sum = [0] * 36
for i in range(6):
    for j in range(6):
        dice_sum[A[i]+B[j]] += 1
print(dice_sum.index(max(dice_sum)))
*/
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a(6), b(6);
    for (auto& itr : a) {
        cin >> itr;
    }
    for (auto& itr : b) {
        cin >> itr;
    }

    vector<int> num_sum(101);
    for (auto& A : a) {
        for (auto& B : b) {
            num_sum[A + B] += 1;
        }
    }

    int mx_num = 0;
    int sum = 0;
    for (int i = 0; i <= 100; i += 1) {
        if (num_sum[i] > mx_num) {
            mx_num = num_sum[i];
            sum = i;
        }
    }

    cout << sum << '\n';
    return 0;
}