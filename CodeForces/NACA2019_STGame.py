#Strange game
#https://www.codechef.com/NACA2019/problems/STGAME
nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    ayushi = sum(sorted([int(x) for x in input().split()])[-2:])
    daksh  = sum(sorted([int(x) for x in input().split()])[-2:])
    if ayushi > daksh: print("AAYUSHI")
    if daksh  >=ayushi:print("DAKSH")

