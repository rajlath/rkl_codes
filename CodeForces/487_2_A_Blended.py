s = input()
o = ["".join(sorted(s[i:i+3])) for i in range(len(s)-2)]
print(("No", "Yes")["ABC" in o])