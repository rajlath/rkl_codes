start_Time = time.time()
for _ in range(10):
    curr = randint(2, 1000000) - 1
    if naive_primality(curr):
        print(curr, "Yes")
    else:
        print(curr, "No")
print("Time taken : {} ".format(time.time() - start_Time))