
class LexOrder():
    def between(self, a, b):
        ret = "IMPOSSIBLE"
        ans = a + "a"
        if ans > a and ans < b:
            return ans
        else:
            return ret

print(LexOrder().between("car", "dog"))


