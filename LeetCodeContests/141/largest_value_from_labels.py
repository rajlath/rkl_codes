#Thanks to yaketake08
class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        value_lbl = sorted([(p, q) for p, q in zip(values, labels)], reverse=True)
        candidate = [0] * 20001
        answer = 0
        counts = 0
        for p, q in value_lbl:
            if candidate[q] == use_limit:continue
            answer += p
            candidate[q] += 1
            counts += 1
            if counts == num_wanted:break
        return answer

print(Solution().largestValsFromLabels([9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2))
