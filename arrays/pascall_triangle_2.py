from collections import deque
class Solution:
    def getRow(self, rowIndex):
        return self.helper(rowIndex, [1])
    
    def helper(self, ri, p):
        if ri==0:
            return p
        ri-=1
        tp=[0]*(len(p)+1)
        l=len(tp)
        for i in range(l):
            if i==0 or i==l-1:
                tp[i]=1
            else:
                tp[i]=p[i]+p[i-1]
        return self.helper(ri, tp)

    def iterative(self, rowIndex):
        prev=[1]
        for i in range(1, rowIndex+1):
            current=[1]*(i+1)
            for j in range(0, i+1):
                if j==0 or j==i:
                    current[j]=1
                else:
                    current[j]=prev[j]+prev[j-1]
            prev=current
        return prev

    #we can calculate the next row from the previous row. 1 3 3 1, makes 4, 6, 4 1, then we add 1 to the beginning (we can do it reversed too)
    def optimal(self, rowIndex):
        p = deque([1])
        for i in range(rowIndex):
            for j in range(i):
                p[j] = p[j] + p[j+1]
            p.appendleft(1)
        return p
    
    def custom_optimal(self, rowIndex):
        prev, current = deque([1] * (rowIndex + 1)), deque([1] * (rowIndex + 1))
        for i in range(rowIndex + 1):
            for j in range(i):
                if j == 0:
                    continue
                else:
                    current[j] = prev[j - 1] + prev[j]                    
            prev, current = current, prev
        return prev


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)