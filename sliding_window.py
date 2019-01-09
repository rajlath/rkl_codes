import collections
class Solution(object):
    '''
    this sliding window implementation tries to find
    a minimum length windows that has entire source
    in target.
    '''

    def min_window(self, source, target):
        left, rite, res_l, res_r, mins = 0, 0, 0, 0, float('inf')
        count_map = collections.Counter(target)
        while rite <= len(source):
            if all(map(lambda i: True if i <= 0 else False, count_map.values())):
                mins = min(mins, rite-left)
                res_l, res_r = left, rite
                if source[left] in count_map:count_map[source[left]] += 1
                left  += 1

            else:
                if rite == len(source):break
                if source[rite] in count_map:count_map[source[rite]] -= 1
                rite += 1
            print(res_l, res_r)
        return source[res_l : res_r]

print(Solution().min_window("ADOBECODEBANC", "ABC"))


