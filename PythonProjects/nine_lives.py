import random
nouns = []
adjective = []
with open("noun.txt", "r") as fn:
    for line in fn:
        nouns.append(line.strip())
with open("adjective.txt", "r") as fa:
    for line in fa:
        adjective.append(line.strip())

def build_word_for_guess():
    secret_word =  random.choice(nouns)+random.choice(adjective)
    return secret_word

def update_clues(guessed_letter, secret_word, clues):
    clue = list(clues)
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_letter:
            clue[i] =  guessed_letter
    return "".join(clue)




lives = 9
heart_symbol = u'\u2764'
word_to_guess = build_word_for_guess()
clues = "?" * len(word_to_guess)

print(word_to_guess)
print("A secret word is behind those question marks.")
guessed = False
while lives > 0:
    print(clues)
    print("You have " + (heart_symbol+" ") * lives + " lives." )
    guessed = input("Enter a letter you guessed in this word. :")
    if guessed in word_to_guess:
        clues = update_clues(guessed,word_to_guess, clues)
        if clues == word_to_guess:
            print(clues)
            guessed = True
            break
    else:
        print("You lost a live. This word is not in the secret word.")
        lives -= 1
        if lives == 0:
            print("You have lost all your lives.")
            guessed = False
            break
if not guessed:
    print("You have failed to guess correct word {}".format(word_to_guess))
else:
    print("You have guess the word :- {} :- right completely.".format(clues))






