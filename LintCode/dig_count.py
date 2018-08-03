def digitCounts(k, n):
        # write your code here
        result = 0
        tmp = k
        while tmp <= n:
            result += (tmp%10 == k)
            if tmp != 0 and tmp//10 == k:
                result += 1
                tmp += 1
            elif tmp //10 == k - 1:
                tmp = tmp + (10 - k)
            else: tmp += 10

        return result

print(digitCounts(2, 302))


