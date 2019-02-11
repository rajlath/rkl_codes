class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        nums = int(''.join(map(str, A))) + K
        return [int(x) for x in str(nums)]