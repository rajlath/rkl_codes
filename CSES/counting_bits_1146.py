# Function which counts set bits from 0 to n
def countSetBits(n) :
    i = 0

    # ans store sum of set bits from 0 to n
    ans = 0

    # while n greater than equal to 2^i
    while ((1 << i) <= n) :

        # This k will get flipped after
        # 2^i iterations
        k = 0

        # change is iterator from 2^i to 1
        change = 1 << i

        # This will loop from 0 to n for
        # every bit position
        for j in range(0, n+1) :
            ans += k

            if change == 1 :

                #  When change = 1 flip the bit
                k = not k

                # again set change to 2^i
                change = 1 << i

            else :
                change -= 1

        # increment the position
        i += 1

    return ans

print(countSetBits(int(input())))