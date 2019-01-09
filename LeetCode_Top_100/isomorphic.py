class Solution:
    def isIsomorphic(self, s, t):
        """
        type s: str
        type t: str
        rtype : bool
        
        """
        src_dict = {}
        tgt_dict = {}
        s_cnt = 0
        t_cnt = 0
        for sc, tc in zip(s, t):
            if sc not in src_dict:
                s_cnt += 1
                src_dict[sc] = s_cnt
            if tc not in tgt_dict:
                t_cnt += 1
                tgt_dict[tc] = t_cnt
            print(src_dict, tgt_dict)    
            if src_dict[sc] != tgt_dict[tc]:
                return False
            
        return True
    
print(Solution().isIsomorphic("eggless", "addmaek"))  
            
    