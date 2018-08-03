'''
Sample Input 0

1
3
Sample Output 0

3
'''
for _ in range(int(input())):
    distance = int(input())
    nos_of_jump = 0
    if distance <=2:
            nos_of_jump = distance
    else:
        a=1
        b=1
        while distance !=0:
            if distance < (a+b):
                nos_of_jump += 1
                a = 1
                b = 0
                distance -= 1
            else:
                nos_of_jump +=2
                distance -= (a+b)
                a = 1
                b +=1
            print(a, b, distance,nos_of_jump)



    print(nos_of_jump)
