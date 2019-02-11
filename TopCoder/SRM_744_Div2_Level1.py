class ThreepartsSplit:
    def split(self, first, last):
        lens = (last - first)//3
        return (first+lens, first+2*lens)


print(ThreepartsSplit().split(10, 14))