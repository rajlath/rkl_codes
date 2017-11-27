'''
Input:

2
33 20
magazinewasstressedduetoitsissues
25 10
dietingbeforeyoudieeating

Output:

Bad
Good
'''
for _ in range(int(input())):
    lens, k = [int(x) for x in input().split()]
    vlen = sum([1 for x in input() if x in 'aeiou'])
    
    print(["Bad","Good"][vlen>k])