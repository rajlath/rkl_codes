'''
class Solution {
    boolean ok(int[] a,int k,double x)
    {
        int n=a.length,tot=0;
        for (int i=0;i<n-1;i++)
        {
            double gap=a[i+1]-a[i];
            int now=(int)Math.ceil(gap/x)-1;
            tot+=now;
            if (tot>k) return false;
        }
        return true;
    }
    public double minmaxGasDist(int[] stations, int K) {
        Arrays.sort(stations);
        double l=0.0,r=stations[stations.length-1]-stations[0];
        while ((r-l)>5e-7)
        {
            double mid=(r+l)/2;
            //if (1==1) return mid;
            if (ok(stations,K,mid)) r=mid; else l=mid;
        }
        return r;
    }
}
'''
import math

class Solution:
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """

        def ok(a,k,x):
            n=len(a)
            tot=0
            for i in range(n-1):
                gap=a[i+1]-a[i]
                now=int(math.ceil(gap/x)-1)
                tot+=now
                if (tot>k): return False
            return True

        stations = sorted(stations)
        l=0.0
        r=stations[len(stations)-1]-stations[0]
        while ((r-l)>(5e-7)):

            mid=(r+l)/2
            if (ok(stations,K,mid)):
                r=mid
            else: l=mid
        return f'{r:.6f}'
        float.

sol = Solution()
print(sol.minmaxGasDist(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9))


