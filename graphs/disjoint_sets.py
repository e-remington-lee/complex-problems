'''
                Union-find Constructor	Find	Union	Connected
Time complexity	    O(N)	             O(1)	 O(N)	 O(1)
'''
class QuickFind(object):
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX is not rootY:
            for i in range(len(self.root)):
                if self.root[i] is rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.root[x] is self.root[y]


# Test Case
# uf = QuickFind(10)
# # 1-2-5-6-7 3-8-9 4
# uf.union(1, 2)
# uf.union(2, 5)
# uf.union(5, 6)
# uf.union(6, 7)
# uf.union(3, 8)
# uf.union(8, 9)
# print(uf.connected(1, 5))  # true
# print(uf.connected(5, 7))  # true
# print(uf.connected(4, 9))  # false
# print(uf.root)
# # 1-2-5-6-7 3-8-9-4
# uf.union(9, 4)
# print(uf.connected(4, 9))  # true
# print(uf.root)
# uf.union(0, 1)
# print(uf.root)

'''
                Union-find Constructor	Find	Union	Connected
Time complexity             	O(N)	O(H)	O(H)	O(H)
'''
class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    '''
    0 0 2
    0 1 2
    '''
    def find(self, x):
        while x is not self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX is not rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) is self.find(y)

# # Test Case
# uf = QuickUnion(10)
# # 1-2-5-6-7 3-8-9 4
# uf.union(1, 2)
# uf.union(2, 5)
# uf.union(5, 6)
# uf.union(6, 7)
# uf.union(3, 8)
# uf.union(8, 9)
# print(uf.connected(1, 5))  # true
# print(uf.connected(5, 7))  # true
# print(uf.connected(4, 9))  # false
# # 1-2-5-6-7 3-8-9-4
# uf.union(9, 4)
# print(uf.connected(4, 9))  # true  

'''
with standard union find which is linear (no dp)
                Union-find Constructor	Find	Union	Connected
Time complexity	                O(N)	O(logN)	O(logN)	O(logN)

with optimized find (dp)
                Union-find Constructor	Find	Union	Connected
Time complexity	                O(N)	O(⍺(N))	O(⍺(N))	O(⍺(N))
'''
class QuickUnionRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if x is not self.root[x]:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        return x

    def find_iterative(self, x):
        stack = []
        while x is not self.root[x]:
            stack.append(x)
            x = self.root[x]
        while stack:
            self.root[stack.pop()] = x
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
    
    def connected(self, x, y):
        return self.find(x) is self.find(y)

# Test Case
uf = QuickUnionRank(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true