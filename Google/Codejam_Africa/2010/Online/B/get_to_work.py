'''
Problem

You work for a company that has E employees working in town T.
There are N towns in the area where the employees live.
You want to ensure that everyone will be able to make it to work.
Some of the employees are drivers and can drive P passengers.
A capacity of P == 1 indicates that the driver can only transport themselves to work.
You want to ensure that everyone will be able to make it to work and you would like to minimize
the number of cars on the road.

You want to calculate the number of cars on the road, with these requirements:

Every employee can get to town T.
The only way an employee may travel between towns is in a car belonging to an employee.
Employees can only take rides from other employees that live in the same town.
The minimum number of cars is used.
Find whether it is possible for everyone to make it to work, and if it is, how many cars will end up
driving to the office.

Input

One line containing an integer C, the number of test cases in the input file.

For each test case there will be:

One line containing the integer N, the number of towns in your area and the integer T, the town
where the office is located.
One line containing the integer E, the number of employees.
E lines, one for each employee, each containing:
An integer H >= 1, the home town of the employee, followed by
An integer P >= 0, the number of passengers they can drive. If the employee is not licensed to drive the number will be 0.
Output

C lines, one for each test case in the order they occur in the input file, each containing the
string "Case #X: " where X is the number of the test case, starting from 1, followed by:
The string IMPOSSIBLE, if there are not enough drivers for everyone to commute; OR
N space-separated integers, one for each town from 1 to N, which indicate the number of vehicles
commuting from the town.
Limits

1 ≤ T ≤ N
1 ≤ H ≤ N
0 ≤ P ≤ 6

Small dataset

C = 50
1 ≤ N ≤ 10
1 ≤ E ≤ 100

Large dataset

C = 100
1 ≤ N ≤ 100
1 ≤ E ≤ 500

Sample


Input

3
5 1
3
1 0
1 0
1 0
5 1
3
2 4
2 0
3 0
5 3
5
1 2
1 0
4 2
4 4
4 0

Output

Case #1: 0 0 0 0 0
Case #2: IMPOSSIBLE
Case #3: 1 0 0 1 0

'''


import sys
from collections import Counter

def get_input_out():
    args = sys.argv
    if len(args) >= 2:
        ins = open(sys.argv[1], "r")
        in_puts = [line for line in ins.readlines()]
        outs = open(sys.argv[2], "w")
        return (in_puts, outs)
    return (None, None)

ins, outs = get_input_out()
if ins is not None:
    index = 0
    tests = 1

    nb_test = int(ins[index])
    index += 1
    for _ in range(nb_test):
        nb_town, office_loc = [int(x) for x in ins[index].split()]
        office_loc -= 1
        index += 1
        nb_employee = int(ins[index])
        index += 1
        employees   = [0] * nb_town
        cars = [[] for _ in range(nb_town)]
        for i in range(nb_employee):
            home_town, capacity = [int(x) for x in ins[index].split()]
            home_town -= 1
            index += 1
            employees[home_town] += 1
            if capacity > 0:
                cars[home_town].append(capacity)
        cars = [sorted(car, reverse = True) for car in cars]
        result = []
        for i in range(nb_town):
            if i == office_loc:
                result.append(0)
                continue
            rem = employees[i]
            used = 0
            for car in cars[i]:
                if rem <= 0:
                   break
                rem -= car
                used+= 1
                if rem > 0:
                    result = None
                    break
                result.append(used)
        if result is None:
            ans1 = "IMPOSSIBLE"
        else:
            ans1 = ' '.join(map(str, result))
        ans = "Case #{}: {}".format(tests, ans1)
        print(ans, file = outs)
        tests += 1

else:
    print("Invalid Input file.")







