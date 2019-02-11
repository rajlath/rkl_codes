key = ''
for i in range(3):
    key += input()
print(["No", "Yes"][key == key[::-1]])