def sum_of_multiples(limit, multiples):
    valid = [0] * (limit+1)
    for i in multiples:
        if i == 0:continue
        j = i
        #print(j)
        while j < (limit):
            #print(j)
            valid[j] = j
            j += i
    return (sum(valid))


#print(sum_of_multiples(1000, [3, 5]))