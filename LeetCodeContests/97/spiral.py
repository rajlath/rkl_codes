class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        d = ( (0,1), (1,0), (0,-1), (-1,0) )
        r = [[r0,c0]]
        st = 0
        di = -1
        for i in range(100000):
            if len(r) == R*C: break
            if i%2==0:
                st+=1
            di = (di+1)%4
            for j in range(st):
                r0 += d[di][0]
                c0 += d[di][1]
                if 0<=r0<R and 0<=c0<C:
                    r.append([r0,c0])
        return r