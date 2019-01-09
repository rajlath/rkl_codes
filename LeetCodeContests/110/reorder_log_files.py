class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """


        lets = sorted([x for x in logs if x.split()[1].islower()], key = lambda a: a.split()[1:])
        digs = [x for x in logs if x.split()[1].isdigit()]
        return lets + digs

print(Solution().reorderLogFiles(["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]))
