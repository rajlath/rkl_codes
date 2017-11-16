for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print(bin( int( a ) ^ int( b ) )[2:].count("1"))
