
class CalkinWilf():
    def findRational(self, st):
        a, b = 1, 1
        for i in st:
            if i == "R":
                a, b = a + b, b
            else:
                a, b = a, a + b
        return (a, b)

print(CalkinWilf().findRational("LRLRLRLRLRLRLRLRLRLRLRLRLRLRLR"))


