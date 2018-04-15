'''
763. Partition Labels
User Accepted: 1077
User Tried: 1143
Total Accepted: 1107
Total Submissions: 1686
Difficulty: Medium
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start_indx_dict = {}
        end_indx_dict   = {}

        for i, s in enumerate(S):
            if s not in start_indx_dict:
                start_indx_dict[s] = i
            end_indx_dict[s] = i

        partitions = []
        index = 0
        while index < len(S):
            start = index
            end   = end_indx_dict[S[start]]
            while index <= end:
                if end < end_indx_dict[S[index]]:
                    end = end_indx_dict[S[index]]
                index += 1
            partitions.append(end - start+1)
            index = end + 1
        return partitions

#solution submitted by Huize Wang  : huizew

sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))





