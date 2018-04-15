class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        mydic={}
        for i in range(len(S)):
            if not mydic.has_key(S[i]): mydic[S[i]]=[i]
            else: mydic[S[i]].append(i)
        res=0
        for w in words:
            if self.get(w, mydic): res+=1
        return res

    def get(self, w, mydic):
        cur=-1
        for c in w:
            if not mydic.has_key(c): return False
            flag=0
            for pos in mydic[c]:
                if pos>cur:
                    flag=1
                    cur=pos
                    break
            if not flag: return False
        return True