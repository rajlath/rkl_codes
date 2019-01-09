""" pig latin conversion"""
def main():
    """ Convert a word into piglatin version
        word starting with consonant:
            shift first word to the last
            add 'ay' to the word at the end
        word starting with a vowel:
            'way' is appended to the word
    """
    while True:
        first_char = ''
        pig_latin = ''
        entered = input("Enter a word ?: \n")
        if entered is None:
            print("You have not entered any word.")
        else:
            first_char = entered[0]
            if first_char in ["a", "e", "i", "o", "u"]:
                pig_latin = entered + "way"
            else:
                pig_latin = entered[1:] + entered[0] + "ay"
            print("Pig Latin version of {} is {}".format(entered, pig_latin))
        print("Do you want to enter another word ?.")
        further = input("Press enter to continue or to quit press space key.")
        if further == " ":
            break


if __name__ == "__main__":
    main()
