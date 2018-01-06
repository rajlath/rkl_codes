class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = str(N)
        ans = [0] * len(N)
        for i in range(len(N)):
            ans[i] = int(N[i])
            if i < len(N) - 1 and N[i] > N[i + 1]:
                while i > 0 and N[i] == N[i - 1]:
                    i -= 1
                #print( i )
                ans[i] -= 1
                for k in range(i + 1, len(N)):
                    ans[k] = 9
                break
        return int("".join([str(x) for x in ans]))

sol = Solution()
print(sol.monotoneIncreasingDigits(12345))

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        s = str(N)
        n = len(s)
        if n==1:
            N
        x = '1' + (n-1) * '0'
        if int(x)==N:
            return int('9' * (n-1) )
        ans = ''
        di = '9876543210'
        for i in xrange(n):
            for j in di:
                cur  = ans + (n-i) * j
                if int(cur) <= N:
                    break
            ans += j
        return int(ans)


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = map(int, str(N))
        good = False
        while not good:
            good = True
            for i in xrange(1, len(num)):
                if num[i] < num[i-1]:
                    num[i-1] -= 1
                    j = i-1
                    while num[j] == -1:
                        num[j] = 9
                        num[j-1] -= 1
                        j -= 1
                    good = False
                    for j in xrange(i, len(num)):
                        num[j] = 9
                    break
            print num
        return int(''.join(map(str, num)))

