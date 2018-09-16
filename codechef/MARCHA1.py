def could_it_be(a, best,sums, req, lens):
    #print(best)
    if sums >  req:  return False
    if sums == req:  return True
    if best >= lens: return False
    sums += a[best]
    could_it_be(a, best+1, sums, req, lens)
    sums -= a[best]
    could_it_be(a, best+1, sums, req, lens)
    return False

nots = int(input())
for _ in range(nots):
    non, req = [int(x) for x in input().split()]
    notes = []
    for _ in range(non): notes.append(int(input()))
    print(["No", "Yes"][could_it_be(notes, 0, 0, req, non)==True])
