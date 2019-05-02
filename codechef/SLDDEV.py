import statistics
nb_boys, k = [int(x) for x in input().split()]
ins = [int(x) for x in input().split()]
for i in range(nb_boys - k + 1):
    curr = ins[i:i+k]
    mean = sum(curr) / k
    sd = 0
    for j in curr:
        sd += (((( j - mean) ** 2)) / k )
    sd = "{:.6f}".format(sd ** 0.5)
    print(sd, end = " ")

