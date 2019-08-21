from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        lens = 0
        cc = Counter(chars)
        #print(cc)
        for i in words:
            ic = Counter(i)
            #print(ic)
            willdo = True
            for j in ic:
                #print(ic[j])
                if cc[j] >= ic[j]:
                    continue
                else:
                    willdo = False
                    break

            if willdo:lens += len(i)
        return lens
'''
wrds = ["leetcode"]
chrs = "welldonehoneyr"