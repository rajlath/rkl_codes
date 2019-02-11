class KidsInAYard:
    def howMany(self, r2, r3, r5):
        incr = 0
        while True:
            current = (incr * 5) + r5
            if current % 3 == r3 and current % 2 == r2:
                if current > 0 :return current
            incr += 1


print(KidsInAYard().howMany(0,0,0))
