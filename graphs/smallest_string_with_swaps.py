class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        from collections import defaultdict
        graph = Dg(len(s))
        
        for x, y in pairs:
            graph.union(x, y)
        
        m = defaultdict(lambda: [])
        for i in range(len(s)):
            index = graph.find(i)
            found_index = self.binary_search(s[i], m[index])
            m[index].insert(found_index, s[i])
        
        response = []
        for i in range(len(s)):
            response.append(m[graph.find(i)].pop(0))
        return "".join(response)
        
        
    def binary_search(self, target, arr):
        if len(arr) is 0:
            return 0
        high = len(arr)-1
        low = 0
        while high >= low:
            mid = (high + low) // 2
            if arr[mid] is target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
        return low
        
        
        
class Dg:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
    def find(self, x):
        if x is not self.root[x]:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        return x
    
    def union(self, x, y):
        if x < y:
            low = x
            high = y
        else:
            low = y
            high = x
        rootX = self.find(low)
        rootY = self.find(high)
        if rootX is not rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1



'''
Takes 2N to make the disjointed graph, E to loop through the edges, N*log(N) to loop throug the string and binary search/insert the map
of javaPractice, then N again to loop through the values and pop off the smallest index each time, then N to join them togther
N*log(n)

space: the map can be number of nodes + N, since if we had map={0:[a b c], 1:[d]} we can't have more than the length of string in there, but we could have
a s nodes, so maybe n+n at worst
'''

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)