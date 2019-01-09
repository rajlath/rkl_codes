#largest subsequence
def calc_cost(a, b):
    score = 0
    for x , y in zip(a, b):
        score += abs((ord(x) - ord(y)))
    return score

def parts_string(str, lens):
    return (str[0+i:lens+i] for i in range(0, len(str), lens))

def main():
    src = input()
    k   = int(input())
    parts = list(parts_string(src, k))
    #print(parts)
    cost = 0
    pat  = parts[0]
    for i in range(1, len(parts)):
        cur_part = parts[i]
        curr = calc_cost(pat, cur_part)
        #print(curr, pat, cur_part)
        cost += curr
    print(cost)









if __name__ == '__main__':
    main()


