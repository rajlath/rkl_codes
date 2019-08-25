class Solution:
def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    cnts = [0] * 11
    for word in words:
        cnts[self.get_freq(word)] += 1
    result = []
    for query in queries:
        freq = self.get_freq(query)
        result.append(0)
        for i in range(freq + 1, 11):
            result[-1] += cnts[i]
    return result

def get_freq(self, word):
    freq = {}
    for c in word:
        freq[c] = freq.get(c, 0) + 1
    for c in range(ord('a'), ord('z') + 1):
        ch = chr(c)
        if freq.get(ch, 0) > 0:
            return freq[ch]
    return 0