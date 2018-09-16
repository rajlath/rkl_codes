class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        words = []
        digit = []
        curr  = ''
        for i in S:
            if i.isdigit():
                digit.append(i)
                if curr != '':
                    words.append(curr)
                curr=''
            else:
                curr += i
        decoded = ''
        for i in words:
            if decoded == '':
                decoded = i
            else:
                decoded += i
            decoded = decoded * int(digit.pop(0))
            print(decoded)
        return decoded[K-1]


class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        l = 0
        i = 0

        while l < K:
            if '0' <= S[i] <= '9':
                l *= int(S[i])
            else:
                l += 1
            i += 1
        i -= 1

        while True:
            if 'a' <= S[i] <= 'z':
                if l == K:
                    return S[i]
                else:
                    l -= 1
            else:
                l //= int(S[i])
                K %= l
                if K == 0: K = l
            i -= 1
        return None
        




print(Solution().decodeAtIndex("ha22",5))