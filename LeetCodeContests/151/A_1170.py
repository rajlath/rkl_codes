from collections import defaultdict
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        accesses = defaultdict(list)
        for i, t in enumerate(transactions):
            name, time, _, city = t.split(',')
            time = int(time)
            accesses[name].append((time, city))
        def invalid(t):
            name, time, amt, city = t.split(',')
            time = int(time)
            if int(amt) > 1000: return True
            return any(c != city and abs(t-time) <= 60 for t, c in accesses[name])
        return filter(invalid, transactions)