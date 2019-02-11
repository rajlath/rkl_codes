class PairProduct:
    def findPair(self, n, A0, step, p):
        '''
        n  :Size of list
        A0 :seed
        step:increment last element by
        p : product of two elements
        '''
        series = []
        series.append(A0)
        for i in range(1, n):
            series.append(series[-1] + step)
        #print(series)
        maybe = []
        for i in range(n):
            if series[i] == 0:continue
            curr = p//series[i]
            if curr == series[i]:
                return(i, i)
            if series[i] in maybe:
                return (maybe.index(series[i]), i)
            else:
                maybe.append(curr)
        return ( )

print(PairProduct().findPair(20,-5,1,-6))

