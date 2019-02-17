def square_of_sum(count):
    return pow(((count * (count + 1)) // 2), 2)


def sum_of_squares(count):
    return sum(i * i for i in range(1, count+1))


def difference(count):
    return abs(sum_of_squares(count) - square_of_sum(count))

#print(difference(10))

