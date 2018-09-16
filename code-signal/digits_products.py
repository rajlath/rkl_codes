def digitsProduct(product):
    if product < 10:
        return product if product > 0 else 10
    r = ""
    for i in range(9,1,-1):
        while product % i == 0:
            product /= i
            r = str(i)  + r;
    return -1 if product != 1 else int(r)

def digitsProduct1(product):
    for p in range(1,10000):
        pt_prod = 1
        for dig in [int(x) for x in list(str(p))]:
            pt_prod *= dig
        if pt_prod == product:
            return p
    else:
        return -1

print(digitsProduct(576))