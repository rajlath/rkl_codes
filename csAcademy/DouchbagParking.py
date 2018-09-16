'''
Douchebag Parking
Time limit: 1000 ms
Memory limit: 256 MB

Consider a row of N parking spots. For each spot you know whether it's free or not, and you are also given its width. You have a car of width WW. Because you are a douchbag, you afford parking on several consecutive parking spots, as longs as they are all free and their total width is greater or equal than WW.

Find the lowest index of a parking spot from a set of consectuive spots where you can park your car.

Standard input
The first line contains two integers NN and WW.

Each of the next NN lines contains two integers: the first integer is equal to 00 or 11, where 00 corresponds to a taken parking spot and 11 to a free one; the second integer is a number L_iL
​i
​​ representing the width of the parking spot.

Standard output
If there is no solution output -1−1.

Otherwise print the answer on the first line.

Constraints and notes
1 \leq N \leq 3001≤N≤300
1 \leq W \leq 3001≤W≤300
1 \leq L_i \leq 300, 1 \leq i \leq N1≤L
​i
​​ ≤300,1≤i≤N
Input	Output	Explanation
5 9
1 3
1 5
0 4
1 2
1 10
4
For the first parking spot, only a car of width smaller of equal to 88 would fit.

For the 44th one, a car with width smaller or equal to 1212 would fit, this being the first parking space that can fit our car of width 99
5 7
1 2
0 3
1 5
1 1
0 2
-1
There's no parking space big enough to fit the car.

4 5
1 2
1 2
1 2
1 2
1
Note that if there are multiple parking places in which the car could be parked, it's required to print the one
'''
nol, need = [int(x) for x in input().split()]
width = 0
ans   = -1
indx  = -1
for i in range(nol):
    p, w = [int(x) for x in input().split()]
    if p == 1:
        if indx == -1:indx = i+1
        width += w
        if width >= need:
            ans = indx
            break
    else:
        width = 0
        indx  = -1
    #print(width, indx)
print(ans)







