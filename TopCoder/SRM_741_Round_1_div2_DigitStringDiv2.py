class DigitStringDiv2():
    def count(self, s, x):
        counts = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = int(s[i:j+1])
                #print(curr)
                counts += (curr > int(x))
        return counts

print(DigitStringDiv2().count("782984137", "44633"))

