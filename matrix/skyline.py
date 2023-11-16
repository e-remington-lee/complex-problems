'''
https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity

https://www.youtube.com/watch?v=GSBLe8cKu0s
'''
import heapq


h= [4,3,1,7,44,7,9,10]

#looks to be a heap min/max version of each operation
heapq.heapify(h)
print(h)
# heapq._heapify_max(h)
# print(heapq.nlargest(1, h)[0])
print(h)
print(heapq._heappop_max(h))
# heapq._heapify_max(h)
print(h)

# heapq.heappop(h)
# print(h)