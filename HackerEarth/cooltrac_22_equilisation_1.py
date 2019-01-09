#largest subsequence
def main():
    src = input()
    k   = int(input())
    pat = src[:k]
    should_be = pat * (len(src) // k)
    #print(should_be)
    cost = 0
    for i in range(len(should_be)):
        cost += abs(ord(src[i]) - ord(should_be[i]))
    print(cost)










if __name__ == '__main__':
    main()


