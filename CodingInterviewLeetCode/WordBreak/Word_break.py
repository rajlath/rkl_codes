def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    memo = [False for i in range(len(s)+1)]
    """
    memo[i] (0<``=i<=len(s)-1) returns the result whether s[:i] could be break successfully.
    Or you can interpret s[:i] as a completely new string s' (a subset of s) whose length is exactly i."""

    memo[0] = True
    """
    if the length of string is 0, no matter how we seperate it, we can't be wrong.
    """
    for i in range(1,len(s)+1):
        """
        we are expanding the substring (i.e. s') of s gradually.
        """
        for j in range(i):
            """
            we are trying all the possibilities to seperate the substring s' to
            check whether it can be broken legally.
            """
            if memo[j] and s[j:i] in wordDict:
                """
                this is the True condition requirement for a good string
                """
                memo[i] = True
    return memo[-1]

print(wordBreak("leetcode", ["leet", "code"]))