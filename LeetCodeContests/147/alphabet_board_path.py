class Solution:
    def alphabetBoardPath(self, target):
        ans = ''
        r, c = 0, 0
        for i in target:
            curr = ord(i) - ord('a')
            tr, tc = divmod(curr, 5)
            if i == "z":
                while c < tc:
                    ans += "R"
                    c += 1
                while c > tc:
                    ans += "L"
                    c -= 1
                while r < tr:
                    ans += "D"
                    r += 1
                while r > tr:
                    ans += "U"
                    r -= 1
            else:
                while r < tr:
                    ans += "D"
                    r += 1
                while r > tr:
                    ans += "U"
                    r -= 1
                while c < tc:
                    ans += "R"
                    c += 1
                while c > tc:
                    ans += "L"
                    c -= 1
            ans+= "!"
        return ans







print(Solution().alphabetBoardPath("code"))
