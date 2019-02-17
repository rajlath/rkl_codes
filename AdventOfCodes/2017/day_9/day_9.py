def get_garbage(segment):
    char_count = 0
    index = 1
    while index < len(segment):
        if segment[index] == ">":
            break
        elif segment[index] == "!":
            index += 2
        else:
            index += 1
            char_count += 1
    return index + 1, char_count

def get_score(segment):
    score, char_count = 0, 0
    index = 0
    stack = [0]
    while index < len(segment):
        if segment[index] == "{":
            score += stack[-1] + 1
            stack.append(len(stack))
            index += 1
        elif segment[index] == "}":
            stack.pop()
            index += 1
        elif segment[index] == "<":
            garb_len, garb_chr = get_garbage(segment[index:])
            index += garb_len
            char_count += garb_chr
        else:
            index += 1
    return score, char_count




if __name__ == '__main__':
    with open(r"E:\rkl_codes\AdventOfCodes\2017\day_9\input.txt") as f:
        lines = f.readlines()
    score, chars = get_score(lines)
    print("Score {} and chars {}".format(score, chars))
