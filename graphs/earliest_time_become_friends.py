class Solution:
    def earliestAcq(self, logs, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        islands = n
        response = -1
        
        for t, x, y in sorted(logs):
            islands -= self.union(x, y)
            if islands == 1:
                return t
        return response
    
    
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
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return 1
        return 0

'''
time: e*log(e) + N + e, we need to sort the logs because we need them in acending order since we need the closest value (soonest?)
space: N for the graph + N for recursion depth of quick sort (average could be log(n))
'''

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)