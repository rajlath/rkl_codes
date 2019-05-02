class Solution:
    def queryString(self, S, N):
        lens = len(S)
        if N > lens * (lens + 1) // 2:
            return False
        valid = [0] * (N + 1)
        valid[0] = True
        for i in range(lens):
            num = 0
            for j in range(i, lens):
                num = num * 2 + int(S[j] == "1")
                if num > N:
                    break
                valid[num] = True
        return all(valid)

class Solution1:
    def queryString(self, S, N):
        valid = set()
        for i in range(len(S)):
            curr = 0
            for j in range(32):
                if i + j >= len(S):break
                curr = curr * 2 + int(S[i + j])
                if curr > N:continue
                if curr == 0:continue
                valid.add(curr)
        return len(valid) == N



print(Solution1().queryString("0110", 3))