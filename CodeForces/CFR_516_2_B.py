for _ in range(int(input())):
    print( 2 ** bin(int(input()))[2:].count("1") )