'''
Two opponents having
h : health
p : strike power
A strike on opponent reduced opponents health by strike power
One of the opponent has healing power hp it increase health by hp
objective is to reduce opponents health to 0
obiviously one having hp can out win opponent by selecting either
heal or strike depending on its health
both strike each other reducing opponents health by their power
Startgey is to check if health is less then opponents strike power
reinforce health by healing power
input
10 6 100
17 5
output
4
STRIKE
HEAL
STRIKE
STRIKE
'''
myhealth, mypower, myhealer = [int(x) for x in input().split()]
oHealth, oPower = [int(x) for x in input().split()]
res = []
while oHealth > 0:
    if myhealth <= oPower and oHealth > mypower:
        myhealth += myhealer-oPower
        res.append("HEAL")
    else:
        res.append("STRIKE")
        oHealth -= mypower
        myhealth -= oPower
print(len(res))
print(*res, sep="\n")
