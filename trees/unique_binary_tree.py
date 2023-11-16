# https://leetcode.com/problems/unique-binary-search-trees/
class Solution:
    def numTrees(self, n: int) -> int:
        m={0:1, 1:1}
        return self.helper(n, m)
        
    def helper(self, n, m):
        if n in m:
            return m[n]
        s = 0
        for i in range(1, n+1):
            s+=self.helper(i-1, m) * self.helper(n-i, m)
        m[n]=s
        return s

    def dynamic_programming(self, n):
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

