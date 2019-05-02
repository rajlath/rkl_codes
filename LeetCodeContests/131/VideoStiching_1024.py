class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        clips = sorted(clips)
        n = len(clips)
        r = i = end = 0
        while end < T:
            target = end
            while i < n and clips[i][0] <= target:
                end = max(end, clips[i][1])
                i += 1
            if end == target: return -1
            r += 1
        return r