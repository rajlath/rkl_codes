class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        num = -1
        a   = [0] * 1000
        while num < K:
            num += 6
            a[0]+= 1
            if num == K: return 0
            i = 0
            while a[i] == 5:
                num += 1
                if num == K: return 0
                a[i] = 0
                i+=1
                a[i] += 1
        return 5


sol = Solution()
print(sol.preimageSizeFZF(1))

'''
public class Solution
{
	public int PreimageSizeFZF(int K)
	{
		int num = -1;
		int[] a = new int[1000];
		while (num < K)
		{
			num += 6; a[0]++;
			if (num == K) return 0;
			int i = 0;
			while (a[i] == 5)
			{
				num++;
				if (num == K) return 0;
				a[i] = 0;
				a[++i]++;
			}
		}
		return 5;
	}
}
'''