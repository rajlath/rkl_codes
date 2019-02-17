class Luhn(object):
    def __init__(self, card_num):
        self.card_num = ''.join(x for x in card_num if x != ' ')


    def is_valid(self):
        #card = "".join(self.card_num.split())
        if len(self.card_num) < 2: return False
        card = [int(x) for x in self.card_num if x.isdigit()]
        #print(card)
        if len(card) != len(self.card_num):
            return False
        #print(card)
        card = card[::-1]
        card = sum([[x*2, (x*2)-9][(x*2)>9] if i%2==1 else x for i,x in enumerate(card)])
        #print(card)
        return card%10==0

print(Luhn("0").is_valid())
