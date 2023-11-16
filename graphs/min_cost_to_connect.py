import heapq
class Solution:
    def minCostConnectPoints(self, points):
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = current = len(points)
        response = 0
        weighted_list = []
        for i in range(n):
            for j in range(i+1, n):
                weight = manhattan(points[i], points[j])
                weighted_list.append([weight, i, j])
                
        # sorted_weights = sorted(weighted_list, key = lambda x: x[2])
        heapq.heapify(weighted_list)
        disjointed_graph = DisjointedGraph(n)
        
        while weighted_list:
            w, i, j = heapq.heappop(weighted_list)
            if disjointed_graph.union(i, j):
                response += w
                current -= 1
            if current == 1:
                break
        return response
        

class DisjointedGraph:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.rank[rootX] += 1
                self.root[rootY] = rootX
            return True
        return False

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

x = 2
y = 3
print(bin(2))
print(bin(3))
xx = x ^ y
yy = x | y
aa = x & y

print(bin(xx))
print(bin(yy))
print(bin(aa))
