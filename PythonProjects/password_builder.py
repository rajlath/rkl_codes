import random
import string


nouns = []
adjective = []
with open("noun.txt", "r") as fn:
    for line in fn:
        nouns.append(line.strip())
with open("adjective.txt", "r") as fa:
    for line in fa:
        adjective.append(line.strip())
punctuations = "!#$*@"
print("      Welcome to password suggestions.     ")
while True:
    numbers = int(input("   How many password suggestion you need ?"))
    print("password suggested for you are :")
    while numbers:
        noun = random.choice(nouns)
        noun = ''.join(noun[0].upper() + noun[1:])
        adj = random.choice(adjective)
        adj = ''.join(adj[0].upper() + adj[1:])
        sym = random.choice(punctuations)
        num = random.randint(10, 99)
        suggested_pass = noun + sym +  adj + str(num)
        print("    " + suggested_pass, end = "\n")
        numbers -= 1
        # print("Password suggested for you is {}  :".format(suggested_pass))
    print()
    print("Would you like a different suggestion ?")
    response = input("Type y for yes and n for n.")
    # response = input("Would you like a different suggestion ? Type y for yes and n for no : ")
    if response == "n":
        break
    

        
        
        
