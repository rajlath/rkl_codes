import heapq

def test_priority_queue(lst):
    if lst == None:return
    heapq.heapify(lst)
    print(lst)
    heapq.heappush(lst, 12)
    heapq.heappush(lst, 32)
    print(lst)
    heapq.heappop(lst)
    print(lst)
    print(len(lst))
    print(lst[0])

test_priority_queue([1, 2, 3])