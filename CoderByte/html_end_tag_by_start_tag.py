import re
def htmlEndTagByStartTag(startTag):
    i = 0
    tag = ''
    while i < len(startTag):
        if startTag[i] == "<":
            j = i + 1
            tag = ''
            while j < len(startTag):
                tag += startTag[j]
                j += 1
                if j == len(startTag):
                    break
                elif startTag[j] in [" ", ">"]:break
            break

        else:i += 1


    return "</" + tag + ">"



print(htmlEndTagByStartTag("<li>"))
