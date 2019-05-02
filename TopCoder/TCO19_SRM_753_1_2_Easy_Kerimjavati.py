from string import ascii_lowercase as al
class KerimJavati():
    def howLong(self, st):
        vals = {}
        curr_val = 1
        for i in al:
            vals[i] = curr_val
            curr_val += 2
        score = 0
        for a in st:
            score += vals[a]
        return score

print(KerimJavati().howLong("hajikerim"))


