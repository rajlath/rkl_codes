R = lambda:[int(x) for x in input().split()]
nb_cards = int(input())
cards    = R()
curr = "sreeja"
sreeja = 0
dima   = 0
while cards:
    if cards[0] > cards[-1]:
        pick = cards[0]
        cards.pop(0)
    else:
        pick = cards[-1]
        cards.pop()

    if curr == "sreeja":
        sreeja += pick
        curr   = "dima"
    else:
        dima += pick
        curr   = "sreeja"
print(sreeja, dima)
