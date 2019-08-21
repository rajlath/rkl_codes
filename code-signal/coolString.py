def coolString(inputString):
    one = [inputString[x] for x in range(0,len(inputString), 2)]
    two = [inputString[x] for x in range(1,len(inputString), 2)]
    return (all(x.isupper() for x in one) and all(x.islower() for x in two) or
            all(x.islower() for x in one) and all(x.isupper() for x in two))

print(coolString("aQwFdA"))
