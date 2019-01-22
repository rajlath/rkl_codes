lens = int(input())
encoded = input()
print (encoded[-2::-2] + encoded[-1::-2][::-1])