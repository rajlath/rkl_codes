def valid_hyphen(s):
    if "-" in s and s.count("-")==3:
        sc = [x for x in s.split()]
        if sum(len(x) for x in sc)==16 and all(len(x)==4 for x in sc) and all(len(set(x))==1 for x in sc):
            return True
    return False


for i in range(int(input())):
    ans = True
    card = input()
    if card[0] in ["4", "5", "6"]:
        if valid_hyphen(s):
            

        if card.count("-") == 3:
            cards = card.split("-")
            if all(len(x)==4 for x in cards):
                if all(len(set(x))==1 for x in cards):
                    if all(x.isdigit() for x in cards):





