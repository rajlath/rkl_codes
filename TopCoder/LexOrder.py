class LexOrder(object):
    def between(self, A, B):
        rets = ''
        for a, b in zip(A, B):
            print(a, b)
            while a == b:
                rets += a
                continue
            if ord(b) - ord(a) < 2:
                return "IMPOSSIBLE"
            rets += chr(ord(a) + 1)
        print('here')
        if rets == a:
            curr = b[len(a) + 1]
            if curr != 'a':
                rets += 'b'
            else:
                return "IMPOSSIBLE"
        return rets

print(LexOrder().between("car","careful"))