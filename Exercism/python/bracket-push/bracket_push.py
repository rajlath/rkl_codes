def is_paired(input_string):
    stack = []
    obracket = "({["
    cbracket = ")}]"
    for i in input_string:
        if i  in obracket or i in cbracket:
            if i in obracket:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if cbracket[obracket.index(last)] != i:
                    return False
    return len(stack) == 0

#print(is_paired("(((185 + 223.85) * 15) - 543)/2"))