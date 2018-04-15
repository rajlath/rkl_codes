'''
var input = S.ToCharArray();

    for(var i = 0; i < input.Length; i++)
    {
        var j = i;

        while(j > 0 && j < input.Length - 1 &&
              (input[j+1] == input[j] || input[j-1] == input[j]))
        {
            var tmp = input[j];
            input[j] = input[j-1];
            input[j-1] = tmp;
            j--;
        }

        if(input[1] == input[0])
        {
            var tmp = input[0];
            input[0] = input[input.Length-1];
            input[input.Length-1] = tmp;
        }
    }

    return new string(input);
'''
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        for i in range(len(S)):
            j = i
            while j > 0 and j < len(S) - 1 and S[j+1] == S[j] or S[j-1] == S[j]:
                S[j], S[j-1] = S[j-1], S[j]
                j-=1

            if S[1] == S[0]:
                S[0], S[len(S)-1] = S[len(S)-1], S[0]
        ans = "".join(S)
        print(ans)
        for i in range(1, len(ans)):
            if ans[i] == ans[i-1]:
                return " "
        return ans


sol = Solution()
print(sol.reorganizeString("bbbbayobq"))
