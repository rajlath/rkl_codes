def factors_sum(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return sum(result) - n


def classify(number):
    if number <= 0:
        raise ValueError("Number has to be posiitve.")
    fs = factors_sum(number)
    if fs > number:
        return "abundant"
    if fs < number:
        return "deficient"
    else:
        return "perfect"


