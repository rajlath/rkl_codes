#largest subsequence
def main():
    ''' a function to find out largest subsequence of near simillar numbers'''
    nb_test = int(input())
    for _ in range(nb_test):
        nb_element = int(input())
        elements   = sorted([int(x) for x in input().split()])
        curr_max   = 1
        maxs       = 0
        for x, y in zip(elements, elements[1:]):
            diff = abs(x - y)
            if diff <= 1:
                curr_max += 1
            else:
                curr_max =  1
            maxs = max(maxs, curr_max)
        print(maxs)


if __name__ == '__main__':
    main()


