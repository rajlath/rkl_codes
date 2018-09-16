def alphabeticShift(inputString):
    return  "".join([chr((ord(x) - ord('a') + 1 + 26)%26 + ord("a")) for x in inputString])

print(alphabeticShift("rajlathz"))