def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)
 
if __name__ == '__main__':
    for d in [[4,2,6,3,8]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))
