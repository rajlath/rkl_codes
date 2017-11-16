
import collections
import heapq
import sys




def huffman(node, result, code=''):
    # Descend the tree recursively creating the codes
    if len(node[2]) > 1:
        huffman(node[3][0], result, code + '0')
        huffman(node[3][1], result, code + '1')
    else:
        result[node[2]] = code


if __name__ == '__main__':
    test_cases = open("code_like_huffman.txt", 'r')
    for line in test_cases:
        ls = line.rstrip('\n')

        f = collections.Counter(ls)        
        h = [(f[s], -1, s, (None, None)) for s in f]
               
        heapq.heapify(h)        

        while(len(h) > 1):
            l, r = heapq.heappop(h), heapq.heappop(h)
            heapq.heappush(h, (l[0] + r[0], l[1] + r[1], l[2] + r[2], (l, r)))
        
        res = dict()
        huffman(h.pop(), res)
        print(res)

        result = ' '.join(('%s: %s;' % (k, res[k]) for k in sorted(res)))
        print(result)

    test_cases.close()
