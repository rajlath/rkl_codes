for _ in range(int(input())):
    lens = int(input())
    given = [int(x) for x in input().split()]
    should = [0] * lens
    for i in range(lens):
        should[i] = given[i] - given[(i + 1) % lens]

    print(["NO", "YES"][should.count(1) == (lens - 1) or should.count(-1) == (lens - 1) ])    
