import random
def FermatPrimalityTest(number):
    if (number > 1):
        for time in range(3):
            randomNumber = random.randint(2, number)-1
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False

        return True
    else:
        return False

p, y = [int(x) for x in input().split()]
ans = -1

for i in range(y,p,-1):
    if FermatPrimalityTest(i):
        ans = i
        break
print(ans)