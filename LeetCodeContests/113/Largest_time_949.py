class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        counts = [0] * 10
        for i in range(4):
            j = A[i]
            while j < 10:
                counts[j] += 1
                j += 1
        if counts[2] == 0:return ""
        startWith = counts[1] == 0
        if startWith and counts[3] == 1:return ""
        if startWith:
             minutes = counts[5] - 2
        else:
            minutes = counts[5] - 1
        if minutes == 0: return ''
        time = [0] * 4
        temp = minutes >= 2 and counts[2] > counts[1]
        startWith1 = startWith or temp
        if startWith1:
            maxs = [2, 3, 5, 9]
        else:
            maxs = [1, 9, 5, 9]
        for i in range(4):
            time[i] = counts.index(counts[maxs[i]])
            for j in range(time[i], 10, 1):
                counts[j]-=1
        return str(time[0])+str(time[1])+":"+str(time[2])+str(time[3])










print(Solution().largestTimeFromDigits([5,5,5,5]))
