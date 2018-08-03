fibo = [1,1]
for i in range(2, 42):
    fibo.append(fibo[-1]+fibo[-2])
print(sum(fibo[:int(input())]))