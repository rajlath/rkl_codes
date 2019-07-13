class Solution:

    def maxSatisfied(self, customers, grumpy, X):
        nb_customers = len(customers)
        '''
        satisfied = sum([y if x == 1 else 0 for x, y in zip(customers, grumpy)])
        satisfied += sum(customers[:X])
        current = satisfied
        for i in range(X, nb_customers):
            if grumpy[i]:current += customers[i]
            if grumpy[i - X]:current -= customers[i - X]
            satisfied = max(satisfied, current)
        return satisfied
        '''
        satisfied = [0] * (nb_customers + 1)
        for i in range(nb_customers):
            satisfied[i+1] = satisfied[i]
            if grumpy[i]:
                satisfied[i + 1] += customers[i]
        nong  = sum([x if y == 0 else 0 for x, y in zip(customers, grumpy)])
        maxs  = 0
        for i in range(X, nb_customers + 1):
            maxs = max(maxs, satisfied[i] - satisfied[i - X])
        return nong + maxs






print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
