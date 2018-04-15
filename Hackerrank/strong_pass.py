numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

lens = int(input())
password = input()
needed   = 0
if not any(x in numbers for x in password):needed+=1
if not any(x in lower_case for x in password):needed+=1
if not any(x in upper_case for x in password):needed+=1
if not any(x in special_characters for x in password):needed+=1

ans  = (0 if lens >=6 else 6  - lens)
print(max(ans, needed))

