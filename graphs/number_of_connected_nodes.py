class Solution:
    def countComponents(self, n: int, edges):
        graph = Dg(n)
        response = n
        
        for x, y in edges:
            response -= graph.union(x, y)
        '''
        If you don't see how each successful union would subtract 1 from the total possible nodes, you can do a regular disjointed graph,
        then do find on each node, adding each find result to a set, return length of set
        for i in range(len(graph.root)):
            root = graph.find(i)
            response.add(root)
            return len(response)
        '''
        return response  

    def DFS(self, n: int, edges):
        li = [[] for i in range(n)]
        visited = [False for i in range(n)]
        ans = 0
        for x, y in edges:
            li[x].append(y)
            li[y].append(x)
            
        for i in range(n):
            if not visited[i]:
                ans += 1
                self.search(li, visited, i)
        return ans
    
    def search(self, li, visited, i):
        visited[i] = True
        for x in li[i]:
            if not visited[x]:
                self.search(li, visited, x)

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
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX is not rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return 1
        else:
            return 0

    

'''
time is O (N + a(m)) where a(m) is ackerman function, esentially constant
space is N for the graph.
'''


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)