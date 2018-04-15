def knapsack(items, values, capacity, count):

    k = [[ 0 for i in range(capacity+1)] for j in range(count+1)]
    for i in range(count):
        for j in range(capacity):
            if i==0 and j == 0:k[i][j] = 0
            elif  values[i-1] <= j:
                k[i][j] = max(values[i - 1] + k[i - 1][j - values[i - 1]], k[i - 1][j])
            else:
                k[i][j] = k[i - 1][j];
    return k[count][capacity]


value = [10, 50, 70 ]
weight = [ 10, 20, 30 ]
capacity = 40;
itemsCount = 3;
result = knapsack(weight,value,capacity,itemsCount);
print(result)











