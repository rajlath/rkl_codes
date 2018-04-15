def binary_expo__iterative(base, power, mods=int(10e9)):
    if power == 0: return 1
    elif power == 1: return base
    else:
        halfn = binary_expo__iterative(base, power//2,mods)
        if power % 2 == 0: return (halfn * halfn)%mods
        else:
            return  (((halfn * halfn) % mods) * base) % mods



def binary_expo_recursive(base, power, mods=int(10e9)):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mods

        base = base * base % mods
        power //= 2
    return result


print(binary_expo__iterative(123, 231))
print(binary_expo_recursive(123, 231))
