'''
If a singular noun ends with ch, x, s, o the plural is formed by adding es. For example, witch -> witches, tomato -> tomatoes.

If a singular noun ends with f or fe, the plural form ends with ves. For example, leaf -> leaves, knife -> knives. Pay attention to the letter f becoming v.

Nouns ending with y change the ending to ies in plural. For example, family -> families.

In all other cases plural is formed by adding s. For example, book -> books.
'''
for _ in range(int(input())):
    s = input()
    if s[-2:] == "ch" or s[-1] in "xso":
        s += "es"
    elif s[-2:] == "fe":
        s = s[:-2] + "ves"
    elif s[-1] == "f":
        s = s[:-1]+"ves"
    elif s[-1] == "y":
        s = s[:-1] + "ies"
    else:s += "s"
    print(s)