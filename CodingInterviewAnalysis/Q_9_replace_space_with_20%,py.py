'''
Question 9
Please implement a function to replace each blank in a string with “%20”.
For instance, it outputs “We%20are%20happy.” if the input is “We are happy.”.
'''
from random import randint, choice
from string import ascii_letters as al

def create_sample_text(lens, nb_spc):
    '''
    create a sample line text of length having spaces as well
    nb_spc = number of space
    '''
    #add space to letter list
    text = []
    for _ in range(lens):
        text .append(al[randint(0, 51)])
    while nb_spc > 0:
        curr = randint(0, lens-1)
        if text[curr] != " " and curr != 0 and curr != lens - 1:
            text[curr] = " "
            nb_spc -= 1
    return ''.join(text)

def replace_space_with_urlspacetag(text):
    nb_space = text.count(" ")
    rets = []
    indx = 0
    for v in text:
        rets.append(v)
        if rets[indx] == ' ':
            rets[indx] = "2"
            rets.append("0")
            rets.append("%")
            indx += 2
        indx += 1
    return "".join(rets)

text = create_sample_text(randint(1, 50), randint(1, 5))
print(text)
print(replace_space_with_urlspacetag(text))






txt = create_sample_text(30, 4)
replace_space_with_urlspacetag(txt)









