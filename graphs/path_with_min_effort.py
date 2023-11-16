import heapq
class Solution:
    def dijkstra(self, heights):
        seen = set()
        y, x = len(heights) - 1, len(heights[0]) - 1
        # effort, val, row, col
        heap = [(0, heights[0][0], 0, 0)]
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            effort, val, row, col = heapq.heappop(heap)
            if row == y and col == x:
                return effort
            
            if (row, col) not in seen:
                seen.add((row, col))
            else:
                continue
                
            for dr, dc in deltas:
                new_row = row + dr
                new_col = col + dc
                if y >= new_row >= 0 and x >= new_col >= 0:
                    height = heights[new_row][new_col]
                    new_effort = max(effort, abs(val - height))
                    heapq.heappush(heap, (new_effort, height, new_row, new_col))
    
    def unionFind(self, heights):
        row = len(heights)
        col = len(heights[0])
        if row == 1 and col == 1:
            return 0

        edge_list = []
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        for cr in range(row):
            for cc in range(col):
                seen.add((cr, cc))
                for dr, dc in deltas:
                    nr = cr + dr
                    nc = cc + dc
                    if (nr, nc) not in seen:
                        if row - 1 >= nr >= 0 and col - 1 >= nc >= 0:
                            difference = abs(heights[cr][cc] - heights[nr][nc])
                            # flatten a matrix cordinates into a linear version of itself!
                            edge_list.append((difference, nr * col + nc, cr * col + cc))                
        edge_list = sorted(edge_list, key = lambda x: x[0])
        union_find = UnionFind(row*col)

        for difference, x, y in edge_list:
            union_find.union(x, y)
            if union_find.find(0) == union_find.find(row*col-1):
                return difference
        return -1                
        
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        
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

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)