class Solution:
    def sumEvenAfterQueries(self, A, queries):
        ans = []
        sums = (sum([x for x in A if not x&1]))
        for i in queries:
            val, indx = i
            was = A[indx]
            now = was + val
            A[indx] = now
            if not was&1:
                if not now&1:
                    sums = sums - was + now
                else:
                    sums = sums - was
            else:
                if not now&1:
                    sums += now
            ans.append(sums)
            #print(A)
        return ans





print(Solution().sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))