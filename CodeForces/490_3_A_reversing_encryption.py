n = int(input())
encoded = input()
for x in range(1, n+1):
    if n % x == 0:
        encoded = encoded[:x][::-1] + encoded[x:]
print(encoded)