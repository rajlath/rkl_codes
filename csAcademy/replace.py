'''
Open the Bottles
Time limit: 1000 ms
Memory limit: 256 MB

You have 33 wine bottles and 33 bottle openers. You know the time necessary to open each bottle using each opener. Find the minimum total time for opening all 33 bottles.

Standard input
The input consists of 33 lines, each containing 33 integers. The jjth number on the iith line is the time necessary to open bottle ii using the opener jj.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq time \leq 1001≤time≤100 for any pair of bottle and bottle opener. All numbers are integers.
You cannot open more bottle simultaneously
Input	Output	Explanation
1 2 2
2 1 2
2 2 1
3
Use bottle opener ii for bottle ii
3 2 7
1 5 8
3 3 10
6
Use opener 22 for bottle 11, opener 11 for bottle 22 and opener 11 or 22 for bottle 33

5 4 3
7 6 11
7 9 2
11
Use bottle openers 33, 22 and 33
'''
o