ins = input()
times = int(input())
results = ''
for i in ins:
    results += chr((ord(i) +(-times) - 97) % 26 + 97)
print(results)