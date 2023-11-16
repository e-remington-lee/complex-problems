import heapq
'''
since heapq does not offer a good max_heap implementation (even though it says it does, test it! it doesnt work), I found you can do this
as a neat replacement. Goes into some depth as a python developer to realize you can use comparators and magic operators like this
'''
li = []
class MaxHeapInt:
    def __init__(self, int):
        self.int = int

    def __lt__(self, other):
        return self.int > other.int
    
    def __str__(self):
        return str(self.int)

heapq.heappush(li, MaxHeapInt(2))
heapq.heappush(li, MaxHeapInt(9))
heapq.heappush(li, MaxHeapInt(4))
heapq.heappush(li, MaxHeapInt(7))
print([x.int for x in li])
print(heapq.heappop(li))
print([x.int for x in li])
print(heapq.heappop(li))
print([x.int for x in li])