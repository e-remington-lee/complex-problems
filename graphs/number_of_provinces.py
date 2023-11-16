class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected[0])
        graph = Dg(n)
        for i in range(len(isConnected)):
            connections = []
            for j in range(i, len(isConnected[i])):
                if isConnected[i][j] is 1 and i is not j:
                    n -= graph.union(i, j)
                '''
                can only get above if you realize that at each following row, you don't need to check the rows before
                1 1 0 
                1 1 0
                0 0 1
                we see that index 0 was unioned with index 1, then when we get to row 2 we only need to see if index 1 joins with any
                following city
                '''
                # if isConnected[i][j] is 1:
                #     connections.append(j)
                # if len(connections) is 2:
                #     y = connections.pop()
                #     n -= graph.union(connections[0], y)
        return n

        
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
                self.rank[rootX] +=1
            return 1
        return 0

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
'''
Time O N^2 + N. it is N^2 bc since we use path finding and union optimization, the cost of a find/union are amortized to be constant time
space: N for the root/rank and response potentially
'''